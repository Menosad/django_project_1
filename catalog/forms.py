from django import forms
from catalog.models import Version, Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
