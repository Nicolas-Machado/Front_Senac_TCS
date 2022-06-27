from urllib import request
from urllib.request import Request
from django.shortcuts import render

def index(request):
    return render(request, 'userPages/homeSenac.html')

def universities(request):
    return render(request, 'userPages/universities.html')

def university(request):
    return render(request, 'userPages/university.html')

def modalities(request):
    return render(request, 'userPages/modalities.html')

def graduationCourses(request):
    return render(request, 'userPages/graduationCourses.html')

def course(request):
    return render(request, 'userPages/courseInfo.html')

def postGraduateCourses(request):
    return render(request, 'userPages/postGraduateCourses.html')

def courseInfo(request):
    return render(request, 'userPages/courseInfo.html')

def login(request):
    return render(request, 'userPages/login.html')

def administration(request):
    return render(request, 'administration/homeAdministration.html')

def courseList(request):
    return render(request, 'administration/courseList.html')

def courseRegistration(request):
    return render(request, 'administration/courseRegistration.html')

def courseMaintenance(request):
    return render(request, 'administration/courseMaintenance.html')
