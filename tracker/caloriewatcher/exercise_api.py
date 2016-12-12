import json
import os
from django.conf import settings


class Exercises():
    def __init__(self):
        path = os.path.join(settings.BASE_DIR, 'caloriewatcher/activity.json')
        exercises_json = open(path)
        self.exs = json.loads(exercises_json.read())

    def get_exercise(self, id):
        for e in self.exs:
            if e['id'] == id:
                return e
        else:
            return False

    def search_exercise(self, kw):
        return [i for i in self.exs if kw in i['Description']]

    def all_exs(self):
        return self.exs