from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse()


def home(request):
    return HttpResponse("Home Page")
