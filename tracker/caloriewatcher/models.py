from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    height = models.IntegerField('user height in cm')
    weight = models.FloatField('user weight in kg')
    born = models.DateTimeField('mm/yyyy')
    gender = models.CharField('user gender in 1 letter', max_length=1)

    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)


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
