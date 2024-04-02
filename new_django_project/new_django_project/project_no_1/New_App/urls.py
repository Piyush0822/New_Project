# urls.py
from django.contrib import admin
from django.urls import path 
from New_App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Log_in', views.Log_in, name='Log_in')  # Corrected URL pattern
]
