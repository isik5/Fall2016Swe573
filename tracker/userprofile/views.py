from django.shortcuts import (render_to_response)
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile_update')

    else:
       user = request.user
       profile = user.profile

       profile.bmi = profile.get_bmi()
       profile.bmr = profile.get_bmr()

       form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('profile.html', args)


def profile_update(request):
    return render_to_response('profile_update.html')


