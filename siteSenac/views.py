from cgi import test
from urllib import request
from urllib.request import Request
from django.shortcuts import render
from datetime import date
from .service import *

def index(request):
    return render(request, 'userPages/homeSenac.html')

def universities(request):
    if 'buscar' in request.GET:
        name = request.GET['buscar']
        response = UniversityService.get_universities_by_name(name)
    else:
        response = UniversityService.get_universities()
    data = {
        'universities': response
    }
    return render(request, 'userPages/universities.html', data)


def university(request, university_id):
    
    print(request.GET)

    university = UniversityService.get_universities_by_id(university_id)
    course = UniversityService.get_courses_in_university(university_id)
    data = {
        'universities': university,
        'courses': course
    }
    return render(request, 'userPages/university.html', data)

def modalities(request):
    return render(request, 'userPages/modalities.html')

def graduationCourses(request):
    #arrumar urgente#
    print(request.GET)

    if 'buscar' in request.GET:
        name = request.GET['buscar']
        response = CourseService.get_courses_by_name(name)
    else:
        response = CourseService.get_courses()
    data = {
        'courses': response
    }
    return render(request, 'userPages/graduationCourses.html', data)

def postGraduateCourses(request):

    print(request.GET)

    if 'buscar' in request.GET:
        name = request.GET['buscar']
        response = CourseService.get_courses_by_name(name)
    else:
        response = CourseService.get_courses()
    data = {
        'courses': response
    }
    return render(request, 'userPages/postGraduateCourses.html', data)

def courseInfo(request, course_id):

    course = CourseService.get_courses_by_id(course_id)
    university = CourseService.get_universities_in_course(course_id)
    data = {
        'universities': university,
        'courses': course
    }

    return render(request, 'userPages/courseInfo.html', data)

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
