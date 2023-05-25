from django.shortcuts import render
from django.http import HttpResponse
from CRUD_App.models import User


def home(request):
    vars = {'name': 'Huzaifa M'}
    return render(request, 'home.html', context=vars)


def create(request):
    return render(request, 'create.html')


def getUsers(request):
    userData = User.objects.all()
    data = {'userData': userData}
    return render(request, 'users.html', context=data)
