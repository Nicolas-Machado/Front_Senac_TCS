from urllib import request
from urllib.request import Request
from django.shortcuts import render

def index(request):
    return render(request, 'homeSenac.html')

def universities(request):
    return render(request, 'locations.html')


def login(request):
    return render(request, 'login.html')


def administration(request):
    return render(request, 'administration.html')