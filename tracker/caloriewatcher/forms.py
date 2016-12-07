from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FoodSearchForm(forms.Form):
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

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.set_password(self.cleaned_data['password1'])
        user.born = self.cleaned_data['born']
        if commit:
            user.save()

        return user


