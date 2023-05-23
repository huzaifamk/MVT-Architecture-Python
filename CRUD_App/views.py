from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Landing Page")


def home(request):
    return HttpResponse("Home Page")


def create(request):
    return render(request, 'CRUD_App/create.html')
