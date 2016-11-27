from django.shortcuts import (render_to_response, render)
from .forms import FoodSearchForm
from caloriewatcher import fcd_api


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
