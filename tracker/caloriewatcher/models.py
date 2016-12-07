from django.contrib.auth.models import User
from django.db import models


class Exercise(models.Model):
    user = models.ForeignKey(User)
    exercise = models.CharField('exercise', max_length=512)
    date_created = models.DateTimeField('date created', auto_created=True)
    # todo: add necessary fields for calculation


class Food(models.Model):
    user = models.ForeignKey(User)
    food = models.CharField('food', max_length=512)
    date_created = models.DateTimeField('date created', auto_created=True)
    # todo: add necessary fields for calculation
