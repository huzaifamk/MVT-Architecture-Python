from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    vars = {'name': 'Huzaifa M'}
    return render(request, 'CRUD_App/home.html', context=vars)


def create(request):
    return render(request, 'CRUD_App/create.html')
