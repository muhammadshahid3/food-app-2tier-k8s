from django import forms
from .models import Food


class FoodForm(forms.ModelForm):
    """Form for creating and updating food records."""

    class Meta:
        model = Food
        fields = ["name", "image", "min_price", "max_price"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter food name"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "min_price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "0.00"}),
            "max_price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "0.00"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        min_price = cleaned_data.get("min_price")
        max_price = cleaned_data.get("max_price")

        if min_price is not None and max_price is not None and min_price > max_price:
            raise forms.ValidationError("Minimum price cannot be greater than maximum price.")

        return cleaned_data
