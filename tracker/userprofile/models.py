from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    height = models.IntegerField('user height in cm', null=True)
    weight = models.FloatField('user weight in kg', null=True)
    born = models.DateTimeField('mm/yyyy', null=True)
    gender = models.CharField('user gender in 1 letter', max_length=1)

    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)