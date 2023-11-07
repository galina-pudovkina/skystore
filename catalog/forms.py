from django import forms
from .models import Product, Version
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ProductForm(forms.ModelForm):
    forbidden_words = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}
    version = forms.ModelChoiceField(queryset=Version.objects.all(), required=False, empty_label="Выберите версию")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            'preview_description',
            'image',
            'category',
            'price',
            'version',
            Submit('submit', 'Сохранить')
        )

    class Meta:
        model = Product
        fields = ['name', 'description', 'preview_description', 'image', 'category', 'price', 'version']

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        if set(name.split()).intersection(self.forbidden_words):
            raise forms.ValidationError(f"Нельзя использовать запрещенное слово в названии продукта.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        if set(description.split()).intersection(self.forbidden_words):
            raise forms.ValidationError(f"Нельзя использовать запрещенное слово в описании продукта.")
        return description

class VersionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VersionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'number',
            'name',
            'is_active',
            Submit('submit', 'Сохранить')
        )

    class Meta:
        model = Version
        fields = ['number', 'name', 'is_active']