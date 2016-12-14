from django import forms
from userprofile.models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('height', 'weight', 'date_of_birth', 'gender', 'bmi', 'bmr')

    def clean_bmi(self):
        bmi = self.cleaned_data['bmi']
        return bmi

    def clean_bmr(self):
        bmr = self.cleaned_data['bmr']
        return bmr
