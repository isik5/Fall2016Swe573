from django.conf import settings
import requests

FCD_API_URL = "http://api.nal.usda.gov/ndb/{0}/?format=json&api_key={1}"
FCD_API_KEY = gBxQKntXgGDh2Jxj4um8bBNayqIvbFGMxC1QWU6F


def get_foods(kw):
    url = FCD_API_URL.format("search", FCD_API_KEY)
    resp = requests.get(url, {"q": kw})
    return resp.json()


def get_reports(ndbno):
    url = FCD_API_URL.format("reports", FCD_API_KEY)
    resp = requests.get(url, {"type": "f", "ndbno": ndbno})
    if not resp.ok:
        resp = requests.get(url, {"type": "f", "ndbno": int(ndbno)})
    return resp.json()


def get_measures(food):
    nutrients = food['report']['food']['nutrients']
    return set(m["label"] for n in nutrients for m in n["measures"])


