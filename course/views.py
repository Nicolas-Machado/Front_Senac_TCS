from django.http import HttpResponse
from django.shortcuts import redirect, render

from course.service import CourseService
from enrollment.service import EnrollmentService
from siteSenac.send_email import Send_EmailService
from siteSenac.service import *
from siteSenac.views import get_user_pass

_NAME = ''
_RESPONSE = ''
_TYPE_COURSE = ''
_UNIVERSITY = ''

def graduationCourses(request):
    global _RESPONSE, _TYPE_COURSE
    response = CourseService.get_courses_graduation()
    _RESPONSE = response
    _TYPE_COURSE = 'graduation'
    data = {
        'courses': response
    }
    return render(request, 'userPages/courseUser/graduationCourses.html', data)

def courses_results_request(response, type_course, university):
    global _TYPE_COURSE, _UNIVERSITY, _RESPONSE
    if response != None:
        _RESPONSE = response
    _TYPE_COURSE = type_course
    if _UNIVERSITY != None:
        _UNIVERSITY = university
    return None

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
    return render(request, 'userPages/courseUser/postGraduateCourses.html', data)


def courseInfo(request, course_id):
    if request.method == 'POST':
        if request.POST['universities'] != '0':
            Send_EmailService.post_send_email(request.POST)

    course = CourseService.get_courses_by_id(course_id)
    university = CourseService.get_universities_in_course(course_id)
    phases = CourseService.get_phases_in_courses(course_id)
    subjects = phases[1]['subjects']
    data = {
        'universities': university,
        'courses': course,
        'phases': phases,
        'subjects': subjects
    }

    return render(request, 'userPages/courseUser/courseInfo.html', data)

def courseList(request):
    if request.user.is_authenticated:
        template = 'administration/courseAdm/courseList.html'
        if 'id' in request.POST:
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            CourseService.put_active_courses(request.POST['id'], token)
            template = 'partials/_admCourse_check_results.html'

        response = CourseService.get_all_courses()
        data = {
            'courses': response
        }
    else:
        return redirect('login')
    return render(request, template, data)

def courseRegistration(request):
    if request.user.is_authenticated:
        template = 'administration/courseAdm/courseRegistration.html'

        if request.method == 'POST':
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            CourseService.post_courses(request.POST, request.FILES, token)
            template = 'administration/courseAdm/courseList.html'

        course = CourseService.get_all_courses()
        data = {
            'courses': course
        }
    else:
        return redirect('administration')
    return render(request, template, data)

def courseSave(request):

    if request.method == 'POST':
        CourseService.post_courses(request.POST, request.FILES)
        course = CourseService.get_courses()

    data = {
        'courses': course
    }
    return render(request, 'administration/courseAdm/courseList.html', data)

def courseMaintenance(request, course_id):
    if request.user.is_authenticated:
        template = 'administration/courseAdm/courseMaintenance.html'
        course = CourseService.get_courses_by_id(course_id)
        if request.method == 'POST':
            template = 'administration/courseAdm/courseList.html'
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            CourseService.put_courses(request.POST, request.FILES, course_id, token)
            course = CourseService.get_all_courses()

        data = {
            'courses': course,
        }
    else:
        return redirect('administration')
    return render(request, template, data)

def courseDetails(request, course_id):
    if request.user.is_authenticated:
        course = CourseService.get_courses_by_id(course_id)
        phases = CourseService.get_phases_in_courses(course_id)
        # subjects = CourseService.get_subjects_in_phases()
        data = {
            'courses': course,
            'phases': phases,
            # 'subjects': subjects
        }
    else:
        return redirect('administration')

    return render(request, 'administration/courseAdm/courseDetails.html', data)

