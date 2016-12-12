from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    height = models.FloatField('Height in cm',  null=True)
    weight = models.IntegerField('Weight in kg', null=True)
    born = models.DateField('Date of Birth', null=True)
    gender = models.CharField('Gender', max_length=1)
    bmi = models.FloatField('BMI', blank=True, null=True)
    bmr = models.FloatField('BMR', blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    def get_bmi(self):
        height_squared = pow(self.height / 100, 2)
        return round(self.weight / height_squared)

    def my_bmi(current_weight, height):

        current_bmi = get_bmi(current_weight, height)
        #   print "current_bmi: ", current_bmi

        bmi_diff = abs(round(healthy_bmi - current_bmi, 2))

        healthy_weight = round((healthy_bmi / 703) * pow(height, 2), 2)

        weight_diff = round(abs(current_weight - healthy_weight), 2)

        percent_diff = round((weight_diff / current_weight) * 100, 2)

        #   print weight_diff

        if current_bmi <= 18:
            print("You're underweight. Go see a doctor!!!! Your BMI is %r" % current_bmi)

        elif current_bmi <= 18.5:
            print("You're thin for your height. Time to chub it up! Your BMI is %r" % current_bmi)

        elif current_bmi <= healthy_bmi:
            print("Relax you're healthy for your height. Your BMI is %r" % current_bmi)

        elif current_bmi <= 29.9:
            print(
                "Your BMI is {}.\nYou need to lose {} on your BMI to get to 24.9.\nThat means losing {} kilograms to get to your max healthy weight of {}.".format(
                    current_bmi, bmi_diff, weight_diff, percent_diff, healthy_weight))
        else:
            print(
                "Your BMI is {}. You're obese. You're over your healthy BMI of 24.9 by {}. That means losing {} kilograms. See the doctor!!!!".format(
                    current_bmi, bmi_diff, weight_diff))

    def get_bmr(self):
        # Women: BMR = 655 + (9.6 x weight in kg) + (1.8 x height in cm) - (4.7 x age in years)
        # Men: BMR = 66 + (13.7 x weight in kg) + (5 x height in cm) - (6.8 x age in years)

        bmr_defaults = ((655, 9.6, 1.8, 4.7), (65, 13.7, 5, 6.8))
        # index_of_bmr as iob
        iob = bmr_defaults[0] if self.gender == "F" else bmr_defaults[1]
        age = datetime.now().year - self.born.year
        return iob[0] + (iob[1] * self.weight) + (iob[2] * self.height) - (iob[3] * age)


class Foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)





