from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.shortcuts import render
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models.signals import pre_save, post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    height = models.FloatField('Height in cm', null=True)
    weight = models.IntegerField('Weight in kg', null=True)
    born = models.DateField('Date of Birth', null=True)
    gender = models.CharField('Gender', max_length=1)
    bmi = models.DecimalField('BMI', blank=True, null=True, max_digits=3, decimal_places=3)

    #User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

    def __unicode__(self):
        return self.user.username


class Foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)


class Bmi(models.Model):
    def get_bmi(self):
        height = self.user.userprofile.height
        weight = self.user.userprofile.weight
        height_squared = pow(height, 2)
        bmi = round(weight / height_squared)

        return bmi

        request.session['bmi'] = util.getBmi()
