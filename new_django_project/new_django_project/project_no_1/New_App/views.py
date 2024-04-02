# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Log_in(request):
    return render(request, 'Log_in.html')
