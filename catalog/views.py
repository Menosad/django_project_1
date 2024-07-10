from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version


class CatalogListView(ListView):
    model = Product
    template_name = "catalog/index.html"


class CatalogTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, *args, **kwargs):
        name = self.request.POST.get("UserName")
        mail = self.request.POST.get("UserEmail")
        phone = self.request.POST.get("UserPhone")
        print(f"Запрос на обратную связь:\n{name}\n{mail}\n{phone}")
        return render(self.request, self.template_name)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"


class ProductCreateView(CreateView):
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('catalog:index')

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
    #     if self.request.method == "POST":
    #         context_data['formset'] = VersionFormset(self.request.POST)
    #     else:
    #         context_data['formset'] = VersionFormset()
    #     context_data['formset'] = VersionFormset
    #     return context_data
    #
    # def form_valid(self, form):
    #     formset = self.get_context_data()['formset']
    #     self.object = form.save()
    #     if form.is_valid() and formset.is_valid():
    #         formset.instance = self.object
    #         formset.save()
    #         print(formset)
    #         #version_number = version.number
    #     return super().form_valid(form)


class ProductUpdateView(UpdateView):
    form_class = ProductForm
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if form.is_valid() and formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        list_objects = super().get_queryset(*args, **kwargs)
        new_list = list_objects.filter(is_published=True)
        return new_list


class BlogCreateView(CreateView):
    model = Blog
    fields = (
        "title",
        "content",
        "preview",
    )

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save()
            obj.slug = slugify(obj.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:detail", args=[self.kwargs.get("pk")])


class BlogUpdateView(UpdateView):
    model = Blog
    fields = (
        "title",
        "content",
        "preview",
    )
    success_url = reverse_lazy("catalog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save()
            obj.slug = slugify(obj.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:detail", args=[self.kwargs.get("pk")])


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:blog_list")
