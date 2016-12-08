from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    height = models.FloatField('Height in cm', null=True)
    weight = models.IntegerField('Weight in kg', null=True)
    born = models.DateField('Date of Birth', null=True)
    gender = models.CharField('Gender', max_length=1)

    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)