from django.contrib.auth import authenticate
from django.shortcuts import (render_to_response, render)
from .forms import FoodSearchForm, MyRegistrationForm
from userprofile.forms import UserProfileForm
from caloriewatcher import fcd_api
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.views import logout
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from userprofile.models import UserProfile


def home(request):
    ctx = {"welcome_text": "conim benim hosgelmissen"}
    return render_to_response('index.html', ctx)


def diary(request):
    ctx = {"food_list": ["buryan kebap", "gavudagi salatasi"]}
    return render_to_response('diary.html', ctx)


def food_search(request):
    ctx = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FoodSearchForm(request.POST)
        ctx['form'] = form
        # check whether it's valid:
        if form.is_valid():
            # search from fcd_api and add to ctx with name "food_search_results"
            kw = form.cleaned_data.get('kw', None)
            if kw:
                foods = fcd_api.get_foods(kw)
                ctx["food_search_results"] = foods
            else:
                pass

                # if a GET (or any other method) we'll create a blank form
    else:
        ctx['form'] = FoodSearchForm()
    return render(request, 'food_search.html', ctx)


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_loggedin.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register_user(request):
    if request.method == 'POST':
        user_form = MyRegistrationForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        # Check if forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user_info = user_form.cleaned_data
            profile_info = profile_form.cleaned_data
            born = profile_info['born']
            gender = profile_info['gender']
            height = profile_info['height']
            weight = profile_info['weight']

            username = user_info['username']
            email = user_info['email']
            password = user_info['password1']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password)
            user.save()
            user.set_password(password)
            user.save()

            profile = UserProfile.objects.create(user=user,
                                                 born=born, gender=gender,
                                                 height=height, weight=weight)
            profile.save()

            new_user = authenticate(username=user_form.cleaned_data['username'])

            login(request)

            return HttpResponseRedirect('/accounts/register_success')

    else:
        user_form = MyRegistrationForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
    args = {}
    args.update(csrf(request))

    args['user_form'] = user_form
    args['profile_form'] = profile_form

    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')
