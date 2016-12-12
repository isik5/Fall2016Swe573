from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Food

class FoodSearchForm(forms.Form):
    kw = forms.CharField(
        max_length=24,

    )

class ExcSearchForm(forms.Form):
    kw = forms.CharField(
        max_length=24,
    )

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    gender = forms.CharField(required=True)
    born = forms.DateField(required=False)
    height = forms.FloatField(required=False)
    weight = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'gender', 'born', 'height', 'weight')

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('ndbno', 'unit', 'serve')

