from urllib import request
from urllib.request import Request
from django.shortcuts import render

def index(request):
    return render(request, 'userpages/homeSenac.html')

def universities(request):
    return render(request, 'userpages/universities.html')

def university(request):
    return render(request, 'userpages/university.html')

def modalities(request):
    return render(request, 'userpages/modalities.html')

def graduationCourses(request):
    return render(request, 'userpages/graduationCourses.html')

def course(request):
    return render(request, 'userpages/courseInfo.html')

def postGraduateCourses(request):
    return render(request, 'userpages/postGraduateCourses.html')

def login(request):
    return render(request, 'userpages/login.html')

def administration(request):
    return render(request, 'administration/homeAdministration.html')

def courseList(request):
    return render(request, 'administration/courseList.html')
