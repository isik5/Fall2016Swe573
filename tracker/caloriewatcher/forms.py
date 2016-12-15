from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Food, Gender


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
    gender = forms.CharField(widget=forms.RadioSelect(choices=Gender.GENDER_CHOICES), required=True)
    date_of_birth = forms.DateField(required=True)
    height = forms.FloatField(required=True)
    weight = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'gender', 'date_of_birth', 'height', 'weight')




class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('ndbno', 'unit', 'serve')

