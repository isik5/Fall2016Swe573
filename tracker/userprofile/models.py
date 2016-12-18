from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    height = models.FloatField('Height in cm',  null=True)
    weight = models.IntegerField('Weight in kg', null=True)
    date_of_birth = models.DateField('Date of Birth', null=True)
    gender = models.CharField('Gender', max_length=1, null=False)
    bmi = models.FloatField('BMI', blank=True, null=True)
    bmr = models.FloatField('BMR', blank=True, null=True)
    note = models.TextField('Notes', blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    def get_bmi(self):
        height_squared = pow(self.height / 100, 2)
        return round(self.weight / height_squared)

    def get_bmr(self):
        # Women: BMR = 655 + (9.6 x weight in kg) + (1.8 x height in cm) - (4.7 x age in years)
        # Men: BMR = 66 + (13.7 x weight in kg) + (5 x height in cm) - (6.8 x age in years)

        bmr_defaults = ((655, 9.6, 1.8, 4.7), (65, 13.7, 5, 6.8))
        # index_of_bmr as iob
        iob = bmr_defaults[0] if self.gender == "F" else bmr_defaults[1]
        age = datetime.now().year - self.date_of_birth.year
        return iob[0] + (iob[1] * self.weight) + (iob[2] * self.height) - (iob[3] * age)

