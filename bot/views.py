from django.http import HttpResponse
from django.views import generic
import requests, json
import pymongo  #this is for c19cd view
from pymongo import MongoClient
from bot.models import Clickboard
from .forms import ClickboardForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

EARTH_RADIUS = 6371.0  #c19cd
MDB_URL = "mongodb+srv://readonly:readonly@covid-19.hip2i.mongodb.net/covid19" #c19cd source

class IndexView(generic.ListView):    #Class-Based View
    template_name = 'bot/index.html'
    model = Clickboard
    context_object_name = 'clickboards_list'


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = ClickboardForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "bot/create_view.html", context)

def c19(request): # this view gets vaccination rate about Belarus from Our world in data
    url = requests.get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json")
    text = url.text
    data = json.loads(text)
    country = data[19] #Belarus is no 19 in the Our World in Data list
    return HttpResponse(json.dumps(country['data']),content_type="application/json")

def c19cd(request):
    client = MongoClient(MDB_URL)
    db = client.get_database("covid19")
    stats = db.get_collection("global_and_us")
    metadata = db.get_collection("metadata")

    # Get some results for the UK:
    print("\nMost recent 10 global_and_us for Belarus:")
    results = (
        stats.find({"country": "United Kingdom", "state": None})
        .sort("date", pymongo.DESCENDING)
        .limit(10)
    )
    return HttpResponse(results)

# Create your views here.
