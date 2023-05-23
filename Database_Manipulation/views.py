from django.shortcuts import render
from django.http import HttpResponse


def Home_v2(request):
    return HttpResponse("Home Page v2")
