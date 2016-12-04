from django.shortcuts import (render_to_response, render)
from .forms import FoodSearchForm
from caloriewatcher import fcd_api
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.views import logout
from django.template.context_processors import csrf


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
