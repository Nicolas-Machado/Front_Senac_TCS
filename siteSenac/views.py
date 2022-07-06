import json
from urllib import response
from django.shortcuts import render
from .service import *

_RESPONSE = ''
_NAME = ''
_TYPE_COURSE = ''
_UNIVERSITY = ''
_USERNAME = '' 
_PASSWORD= ''

def index(request):
    return render(request, 'userPages/homeSenac.html')

def services(request):
    return render(request, 'userPages/services.html')

def modalities(request):
    return render(request, 'userPages/modalities.html')

def contact(request):
    response = UniversityService.get_all_universities()

    data = {
        'universities': response
    }
    return render(request, 'userPages/contact.html', data)

    
#-------------------------------------------------------------------------------------------------------------START COURSE VIEWS--------------------------------------------------------------------------------------


def graduationCourses(request):
    global _RESPONSE, _TYPE_COURSE
    response = CourseService.get_courses_graduation()
    _RESPONSE = response
    _TYPE_COURSE = 'graduation'
    data = {
        'courses': response
    }
    return render(request, 'userPages/graduationCourses.html', data)

def courses_results(request):
    global _RESPONSE, _NAME
    template = ''

    if 'search' in request.POST:
        _NAME = request.POST['search']
        if _TYPE_COURSE == 'graduation':
            response = CourseService.get_courses_graduation_by_name(_NAME)
        elif _TYPE_COURSE == 'university_course':
            response = CourseService.get_courses_in_university_by_name(_UNIVERSITY['id'], _NAME)
        elif _TYPE_COURSE == 'post_graduation':
                response = CourseService.get_courses_postgraduation_by_name(_NAME)
        _RESPONSE = response
        template = 'partials/_courses_results.html'
    
    if 'switchSubscription' in request.POST:
        if _NAME == '':
            response = EnrollmentService.search_date_enrollment_activate(_RESPONSE)
        else:
            if _TYPE_COURSE == 'graduation':
                response = CourseService.get_courses_graduation_by_name(_NAME)
            elif _TYPE_COURSE == 'university_course':
                response = CourseService.get_courses_in_university_by_name(_UNIVERSITY['id'], _NAME)
            elif _TYPE_COURSE == 'post_graduation':
                response = CourseService.get_courses_postgraduation_by_name(_NAME)
            response = EnrollmentService.search_date_enrollment_activate(response)
        template = 'partials/_courses_results.html'
    else:
        if _NAME == "":
            response = _RESPONSE
        else:
            if _TYPE_COURSE == 'graduation':
                response = CourseService.get_courses_graduation_by_name(_NAME)
            elif _TYPE_COURSE == 'university_course':
                response = CourseService.get_courses_in_university_by_name(_UNIVERSITY['id'], _NAME)
            elif _TYPE_COURSE == 'post_graduation':
                response = CourseService.get_courses_postgraduation_by_name(_NAME)
        template = 'partials/_courses_results.html'
    data = {
        'courses': response
    }
    return render(request, template, data)

def postGraduateCourses(request):
    global _RESPONSE, _TYPE_COURSE
    response = CourseService.get_courses_postgraduation()
    _RESPONSE = response
    _TYPE_COURSE = 'post_graduation'
    data = {
        'courses': response
    }
    return render(request, 'userPages/postGraduateCourses.html', data)

def courseInfo(request, course_id):

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

def courseList(request):
    template = 'administration/courseList.html'
    if 'id' in request.POST:
        token = adm_authenticate(_USERNAME, _PASSWORD)
        CourseService.put_active_courses(request.POST['id'], token)
        template = 'partials/_admCourse_check_results.html'

    response = CourseService.get_all_courses()
    data = {
        'courses': response
    }
    return render(request, template, data)

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

def courseMaintenance(request, course_id):

    course = CourseService.get_courses_by_id(course_id)
    data = {
        'courses': course,
    }
    return render(request, 'administration/courseMaintenance.html', data)


#-------------------------------------------------------------------------------------------------------------END COURSE VIEWS--------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------START UNIVERSITY VIEWS--------------------------------------------------------------------------------------


def universities(request):
    template = ''
    if 'search' in request.GET:
        name = request.GET['search']
        response = UniversityService.get_universities_by_name(name)
        template = 'partials/_universities_results.html'
    else:
        response = UniversityService.get_universities()
        template = 'userPages/universities.html'
    data = {
        'universities': response
    }
    return render(request, template, data)

def university(request, university_id):
    global _RESPONSE, _TYPE_COURSE, _UNIVERSITY
    if request.method == 'POST':
        Send_EmailService.post_send_email(request.POST)

    university = UniversityService.get_universities_by_id(university_id)
    course = CourseService.get_courses_in_university(university_id)
    _RESPONSE = course
    _UNIVERSITY = university
    _TYPE_COURSE = 'university_course'
    data = {
        'universities': university,
        'courses': course
    }
    return render(request, 'userPages/university.html', data)

def universityList(request):
    template = 'administration/universityList.html'
   
    if 'id' in request.POST:
        token = adm_authenticate(_USERNAME, _PASSWORD)
        UniversityService.put_active_universities(request.POST['id'], token)
        template = 'partials/_admUniversity_check_results.html'

    response = UniversityService.get_all_universities()
    data = {
        'universities': response
    }
    
    return render(request, template, data)

def universityRegistration(request):
    if request.method == 'POST':
        UniversityService.post_university(request.POST)
        
    response = CourseService.get_courses()
    data = {
        'courses': response
    }
    return render(request, 'administration/universityRegistration.html', data)

def universityMaintenance(request, university_id):

    university = UniversityService.get_universities_by_id(university_id)
    course = CourseService.get_courses()
    data = {
        'universities': university,
        'courses': course
    }
    return render(request, 'administration/universityMaintenance.html', data)


#-------------------------------------------------------------------------------------------------------------END UNIVERSITY VIEWS--------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------SOME ADMINISTRATION VIEWS--------------------------------------------------------------------------------------


def administration(request):
   return render(request, 'administration/homeAdministration.html')

def login(request):
    return render(request, 'userPages/login.html')

def login_authentication(request):
    global _USERNAME, _PASSWORD
    _USERNAME = request.POST['username']
    _PASSWORD = request.POST['password']
    token = adm_authenticate(_USERNAME, _PASSWORD)
    template = 'administration/homeAdministration.html'
    if token == None:
        template = 'userPages/login.html'
    return render(request, template)

def schoolProgramRegistration(request):

    course = CourseService.get_courses()

    data = {
        'courses': course,
    }
    return render(request, 'administration/schoolProgramRegistration.html', data)

def subjectRegistration(request):
    return render(request, 'administration/subjectRegistration.html')
#-------------------------------------------------------------------------------------------------------------END ADMINISTRATION VIEWS--------------------------------------------------------------------------------------
