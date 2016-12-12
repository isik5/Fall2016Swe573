from django.db.models import Count
from django.shortcuts import (render_to_response, render)
from django.utils.datetime_safe import datetime
from caloriewatcher.exercise_api import Exercises
from caloriewatcher.models import Food, Exercise
from .forms import FoodSearchForm, MyRegistrationForm, AddFoodForm, \
    ExcSearchForm
from userprofile.forms import UserProfileForm
from caloriewatcher import fcd_api
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile


def home(request):
    return render_to_response('index.html',
                                {'full_name': request.user.username})


@login_required
def diary(request):
    day = request.GET.get('date', datetime.today())
    ctx = dict()
    ctx['day'] = datetime.strptime(day, '%m/%d/%Y')
    ctx['all_food'] = Food.objects.filter(user=request.user, date_consumed=ctx['day'])

    ctx['all_exercises'] = Exercise.objects.filter(user=request.user, date_created=ctx['day'])

    ctx['summary'] = {
        'get_daily_consumed': sum(i.get_food_calorie for i in ctx['all_food']),
        'get_daily_burned': sum(i.get_total_mets for i in ctx['all_exercises']),
    }
    profile = UserProfile.objects.get(user=request.user)
    ctx['summary']['left'] = int(
        profile.get_bmr() - ctx['summary']['get_daily_consumed'] + ctx['summary']['get_daily_burned'])
    ctx['summary']['bmr'] = int(profile.get_bmr())

    return render_to_response('diary.html', ctx)

@login_required
def food_search(request):
    ctx = {}
    todays_food = Food.objects.filter(date_consumed=datetime.today(), user=request.user)
    ctx['todays_food'] = todays_food
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


@login_required
def add_food(request):
    ndbnos = request.POST.getlist('add-ndbno')
    if len(ndbnos) > 0:
        foods = [fcd_api.get_reports(no) for no in ndbnos]
        food_with_server = [{"food": food, "serve": fcd_api.get_measures(food)} for food in foods]
        c = {'foods': food_with_server}
        c.update(csrf(request))
        return render_to_response('diary.html', c)
    else:
        food_form = AddFoodForm(request.POST)
        if food_form.is_valid():
            food_form.instance.user = request.user
            food_form.instance.date_consumed = datetime.today()
            food = food_form.save()
        return HttpResponseRedirect('/food-search/')


@login_required
def exc_search(request):
    ctx = {}
    todays_exc = Exercise.objects.filter(date_created=datetime.today(),
                                      user=request.user)
    ctx['todays_exc'] = todays_exc
    if request.method == 'POST':
        kw = request.POST.get('kw', None)
        ex_ids = request.POST.getlist('add-exc', None)
        excs = Exercises()
        if kw:
            form = ExcSearchForm(request.POST)
            ctx['form'] = form
            if form.is_valid():
                ctx["excs"] = excs.search_exercise(kw)
        if ex_ids:
            if len(ex_ids) > 0:
                rp = request.POST
                exercises = []
                for e in ex_ids:
                    min = (float(rp.get("min-{}".format(e))))
                    if min > 0:
                        exercises.append(
                            Exercise(
                                minute=min,
                                user=request.user,
                                date_created = datetime.today(),
                                exercise=e
                            )
                        )
                if len(exercises) > 0:
                    Exercise.objects.bulk_create(exercises)
                    return HttpResponseRedirect('/exercise-search')
    else:
        ctx['form'] = ExcSearchForm()
    return render(request, 'exercise_search.html', ctx)


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
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_loggedin.html')


@login_required
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register_user(request):
    if request.method == 'POST':
        user_form = MyRegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST, files=request.FILES)
        # Check if forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.instance.user = user
            profile_form.save()

            return HttpResponseRedirect('/accounts/register_success')

    else:
        user_form = MyRegistrationForm()
        profile_form = UserProfileForm()
    args = {}
    args.update(csrf(request))

    args['user_form'] = user_form
    args['profile_form'] = profile_form

    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')
