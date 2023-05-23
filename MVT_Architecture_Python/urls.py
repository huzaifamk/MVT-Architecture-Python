# Django Version: 3.1.7

from django.contrib import admin
from django.urls import path
from CRUD_App import views as v1
from Database_Manipulation import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.index, name='index'),
    path('home/', v1.home, name='home'),
    path('home/v2', v2.Home_v2, name='home_v2'),
]
