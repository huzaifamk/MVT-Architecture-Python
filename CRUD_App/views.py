from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'CRUD_App/index.html')


def home(request):
    return render(request, 'CRUD_App/home.html')


def create(request):
    return render(request, 'CRUD_App/create.html')
