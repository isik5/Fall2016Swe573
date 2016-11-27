from django.conf import settings
import requests

FCD_API_URL = "http://api.nal.usda.gov/ndb/{0}/?format=json&api_key={1}"
FCD_API_KEY = settings.FCD_API_KEY


def get_foods(kw):
    url = FCD_API_URL.format("search", FCD_API_KEY)
    resp = requests.get(url, {"q": kw})
    return resp.json()


def get_reports(ndbno):
    url = FCD_API_URL.format("reports", FCD_API_KEY)
    resp = requests.get(url, {"type": "f", "ndbno": ndbno})
    return resp.json()
