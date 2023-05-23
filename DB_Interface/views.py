from django.shortcuts import render
from django.http import HttpResponse


def home_v3(request):
    return HttpResponse("Home Page v3")


def home_v4(request):
    return HttpResponse("Home Page v4")
