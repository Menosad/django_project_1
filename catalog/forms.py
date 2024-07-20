from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import BooleanField

from catalog.models import Version, Product

forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)


class ValidationFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(ValidationFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        name = self.cleaned_data.get('name').lower()
        for word in forbidden_words:
            if word in name:
                raise forms.ValidationError(f"недопустимо использовать {word}")
        return name


class VersionForm(ValidationFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
        #exclude = ('number',)

    def clean_name(self):
        name = self.cleaned_data.get('name').lower()
        for word in forbidden_words:
            if word in name:
                raise forms.ValidationError(f"недопустимо использовать {word}")
        return name


AuthenticationForm