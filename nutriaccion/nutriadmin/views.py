from django.shortcuts import render
from django.http import HttpResponse
from .nutria import demo as domo


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_hfaz(request):
    return HttpResponse(domo.hfaz.to_html())
