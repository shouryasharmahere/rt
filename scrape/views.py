from django.shortcuts import render 
from django.template import loader
from django.http import HttpResponse
from .models import Website

# Create your views here.

def index(request):
    template = loader.get_template("scrape/index.html")
    return HttpResponse(template.render())