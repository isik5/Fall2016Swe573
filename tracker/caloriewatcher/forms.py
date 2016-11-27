from django import forms


class FoodSearchForm(forms.Form):
    kw = forms.CharField(
        max_length=24,
    )
