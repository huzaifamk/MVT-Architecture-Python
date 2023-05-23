from django.urls import path
from DB_Interface import views

urlpatterns = [
    path('', views.home_v3, name='home_v3'),
    path('home/', views.home_v4, name='home_v4'),
]
