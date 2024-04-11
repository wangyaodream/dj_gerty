from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    return HttpResponse("Hello Index.")


def members(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())


def get_list(request):
    return HttpResponse("This is a response")

