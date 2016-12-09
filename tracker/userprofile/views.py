from django.shortcuts import (render_to_response, render)
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        form.user = request.user

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/accounts/profile_update')

    else:

        profile_obj = UserProfile.objects.get(user=request.user)
        weight = profile_obj.weight
        height = profile_obj.height
        height_squared = pow(height, 2)
        bmi = round(request, weight / height_squared)


        return render('profile.html', {'bmi': bmi})


def profile_update(request):
    return render_to_response('profile_update.html')

