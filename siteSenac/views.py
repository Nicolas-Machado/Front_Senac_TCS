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

    if request.method == 'POST':
        Send_EmailService.post_send_email(request.POST)

    university = UniversityService.get_universities_by_id(university_id)
    course = UniversityService.get_courses_in_university(university_id)
    data = {
        'universities': university,
        'courses': course
    }
    return render(request, 'userPages/university.html', data)

def graduationCourses(request):

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

    if 'buscar' in request.GET:
        name = request.GET['buscar']
        response = CourseService.get_courses_by_name(name)
    else:
        response = CourseService.get_courses()
    data = {
        'courses': response
    }
    return render(request, 'userPages/postGraduateCourses.html', data)

def courseInfo(request, course_id,):

    course = CourseService.get_courses_by_id(course_id)
    university = CourseService.get_universities_in_course(course_id)
    phases = CourseService.get_phases_in_courses(course_id)
    # subjects = CourseService.get_subjects_in_phases()
    data = {
        'universities': university,
        'courses': course,
        'phases': phases,
        # 'subjects': subjects
    }

    return render(request, 'userPages/courseInfo.html', data)

def modalities(request):
    return render(request, 'userPages/modalities.html')

def services(request):
    return render(request, 'userPages/services.html')

def login(request):
    return render(request, 'userPages/login.html')

def administration(request):
    return render(request, 'administration/homeAdministration.html')

def courseList(request):

    if 'buscar' in request.GET:
        name = request.GET['buscar']
        response = CourseService.get_courses_by_name(name)
    else:
        response = CourseService.get_courses()
    data = {
        'courses': response
    }

    return render(request, 'administration/courseList.html', data)

def universityList(request):

    if 'buscar' in request.GET:
        name = request.GET['buscar']
        response = UniversityService.get_universities_by_name(name)
    else:
        response = UniversityService.get_universities()
    data = {
        'universities': response
    }
    
    return render(request, 'administration/universityList.html', data)

def courseRegistration(request):
    return render(request, 'administration/courseRegistration.html')

def courseSave(request):

    print(request.FILES)

    if request.method == 'POST':
        CourseService.post_courses(request.POST, request.FILES)
        course = CourseService.get_courses()

    data = {
        'courses': course
    }
    
    return render(request, 'administration/courseList.html', data)

def universityRegistration(request):

    if 'buscar' in request.GET:
        name = request.GET['buscar']
        response = CourseService.get_courses_by_name(name)
    else:
        response = CourseService.get_courses()
    data = {
        'courses': response
    }

    return render(request, 'administration/universityRegistration.html', data)

def courseMaintenance(request, course_id):

    course = CourseService.get_courses_by_id(course_id)
    data = {
        'courses': course,
    }

    return render(request, 'administration/courseMaintenance.html', data)

def universityMaintenance(request, university_id):

    university = UniversityService.get_universities_by_id(university_id)
    course = CourseService.get_courses()
    data = {
        'universities': university,
        'courses': course
    }
    return render(request, 'administration/universityMaintenance.html', data)