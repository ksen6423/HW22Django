from django import forms

from catalog.models import Product

forbid_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


def validate_no_forbid_words(value):
    lower_value = value.lower()
    for word in forbid_words:
        if word in lower_value:
            raise forms.ValidationError(f"Слово '{word}' запрещено.")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        name = forms.CharField(
            max_length=100,
            validators=[validate_no_forbid_words],
        )

        description = forms.CharField(
            widget=forms.Textarea,
            validators=[validate_no_forbid_words]
        )

        website = forms.CharField(
            required=False,
            widget=forms.HiddenInput,
            label=""
        )

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Название"})
        self.fields["description"].widget.attrs.update({"class": "form-control", "rows": 4})
        self.fields["price"].widget.attrs.update({"class": "form-control", "min": "0"})

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Обнаружен спам-бот.")
        return self.cleaned_data.get("website")

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("status", "name")
