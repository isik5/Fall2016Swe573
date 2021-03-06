from django.contrib.auth.models import User
from django.db import models
from .fcd_api import get_reports
from .exercise_api import Exercises
from userprofile.models import UserProfile


class Exercise(models.Model):
    user = models.ForeignKey(User)
    exercise = models.IntegerField('exercise')
    date_created = models.DateField('date created', auto_now_add=True)
    minute = models.IntegerField('minute')


    @property
    def get_exercise(self):
        e = Exercises()
        return e.get_exercise(self.exercise)

    @property
    def get_total_mets(self):
        e = Exercises()
        # kcal / min = METs x body weight in kilograms / 60

        return e.get_exercise(self.exercise)["METS"] * self.minute


class Food(models.Model):
    user = models.ForeignKey(User)
    date_consumed = models.DateField('date consumed', auto_now_add=True)
    ndbno = models.CharField('ndbno', max_length=512)
    unit = models.CharField('unit', max_length=512)
    serve = models.IntegerField('serve')

    @property
    def get_food(self):
        food = get_reports(self.ndbno)
        return food['report']['food']

    @property
    def get_food_calorie(self):
        food = get_reports(self.ndbno)
        for m in food['report']['food']['nutrients']:
            if m['unit'] == 'kcal':
                return int(m['value']) * self.serve



class Gender(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)