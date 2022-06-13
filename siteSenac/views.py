from urllib import request
from urllib.request import Request
from django.shortcuts import render

def index(request):
    return render(request, 'homeSenac.html')

def universities(request):
    return render(request, 'universities.html')

def university(request):
    return render(request, 'university.html')

def modalities(request):
    return render(request, 'modalities.html')

def graduationCourses(request):
    return render(request, 'graduationCourses.html')

def login(request):
    return render(request, 'login.html')


def administration(request):
    return render(request, 'administration.html')
