# Django Version: 3.1.7

from django.contrib import admin
from django.urls import path
from CRUD_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
