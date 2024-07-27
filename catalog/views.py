from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
from catalog.models import Product, Blog, Version, Category
from catalog.services import get_product_list_from_cache
from config import settings


class CategoriesListView(ListView):
    model = Category
    template_name = 'catalog/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        for obj in context['object_list']:
            obj.products_count = len(obj.products.all())
            obj.save()
        return context


class CategoryDetailView(DetailView):
    model = Category

    def get_object(self, queryset=None):
        cat = super().get_object()
        cat.prod_list = get_product_list_from_cache(self.kwargs['pk'])
        cat.save()
        return cat


class CatalogTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, *args, **kwargs):
        name = self.request.POST.get("UserName")
        mail = self.request.POST.get("UserEmail")
        phone = self.request.POST.get("UserPhone")
        print(f"Запрос на обратную связь:\n{name}\n{mail}\n{phone}")
        return render(self.request, self.template_name)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object
        versions_list = Version.objects.filter(product__pk=obj.pk)
        if len(versions_list) > 0:
            context['versions_list'] = versions_list
        version_query_set = Version.objects.filter(product__pk=obj.pk).filter(is_current=True)

        if len(version_query_set) == 1:
            version = version_query_set.get()
            context['version'] = version
        return context


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('catalog:main')

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if form.is_valid() and formset.is_valid():
            self.object.owner = self.request.user
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ProductForm
    model = Product
    login_url = 'users:users_login'

    def test_func(self):
        pk = self.kwargs.get('pk')
        owner = Product.objects.get(pk=pk).owner
        return self.request.user == owner

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
        num = 0
        for version in formset.cleaned_data:
            if version['is_current']:
                num += 1
        if num > 1:
            form.add_error(None, 'У продукта не может быть больше одной актуальной версии')
            return self.form_invalid(form)
        else:
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


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    login_url = 'users:users_login'
    fields = (
        "title",
        "content",
        "preview",
    )

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save()
            user = self.request.user
            obj.owner = user
            obj.slug = slugify(obj.title)
            obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:detail", args=[self.kwargs.get("pk")])


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    login_url = 'users:users_login'
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


class VersionDetailView(DetailView):
    model = Version

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.object.product.pk)
        context['product'] = product
        return context


class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = Version
    success_url = 'catalog/category_detail.html'
    login_url = 'users:users_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.object.product.pk)
        context['product'] = product
        return context
