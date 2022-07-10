from django.shortcuts import redirect, render
from course.service import CourseService
from enrollment.service import EnrollmentService
from siteSenac.send_email import Send_EmailService
from subject.service import SubjectService
from siteSenac.service import *
from siteSenac.views import get_user_pass
from django.contrib import messages

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


def search_results():
    if _TYPE_COURSE == 'graduation':
        response = CourseService.get_courses_graduation_by_name(_NAME)
    elif _TYPE_COURSE == 'university_course':
        response = CourseService.get_courses_in_university_by_name(
            _UNIVERSITY['id'], _NAME)
    elif _TYPE_COURSE == 'post_graduation':
        response = CourseService.get_courses_postgraduation_by_name(_NAME)
    return response


def switch_results():
    if _NAME == '':
        if _TYPE_COURSE == 'university_course':
            response = EnrollmentService.search_date_enrollment_activate(
                _RESPONSE, _UNIVERSITY['id'])
        else:
            response = EnrollmentService.search_date_enrollment_activate(
                _RESPONSE, None)
    else:
        if _TYPE_COURSE == 'graduation':
            response = CourseService.get_courses_graduation_by_name(_NAME)
        elif _TYPE_COURSE == 'university_course':
            response = CourseService.get_courses_in_university_by_name(
                _UNIVERSITY['id'], _NAME)
        elif _TYPE_COURSE == 'post_graduation':
            response = CourseService.get_courses_postgraduation_by_name(_NAME)
        response = EnrollmentService.search_date_enrollment_activate(
            response, None)
    return response


def occupation_area_results(occupation_area):
    response = []
    courses = []
    if occupation_area != 'Area de atuação':
        if _NAME != "":
            if _TYPE_COURSE == 'graduation':
                courses = CourseService.get_courses_graduation_by_name(_NAME)
            elif _TYPE_COURSE == 'university_course':
                courses = CourseService.get_courses_in_university_by_name(
                    _UNIVERSITY['id'], _NAME)
            elif _TYPE_COURSE == 'post_graduation':
                courses = CourseService.get_courses_postgraduation_by_name(
                    _NAME)

            for course in courses:
                if course['occupation_area'] == occupation_area:
                    response.append(course)
        else:
            if _TYPE_COURSE == 'graduation':
                response = CourseService.get_courses_graduation_occupation_area(
                    occupation_area)
            elif _TYPE_COURSE == 'university_course':
                response = CourseService.get_courses_in_university_occupation_area(
                    _UNIVERSITY['id'], occupation_area)
            elif _TYPE_COURSE == 'post_graduation':
                response = CourseService.get_courses_pos_graduation_occupation_area(
                    occupation_area)
    else:
        response = search_results()
    return response


def courses_results(request):
    global _RESPONSE, _NAME

    if 'search' in request.POST:
        _NAME = request.POST['search']
        response = search_results()
        _RESPONSE = response

    if 'switchSubscription' in request.POST:
        response = switch_results()
    else:
        response = _RESPONSE

    if 'occupationArea' in request.POST:
        occupation_area = request.POST['occupationArea']
        response = occupation_area_results(occupation_area)
        _RESPONSE = response

    data = {
        'courses': response
    }

    return render(request, 'partials/coursePartials/_courses_results.html', data)


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

    data = {
        'universities': university,
        'courses': course,
        'phases': phases,
    }

    return render(request, 'userPages/courseUser/courseInfo.html', data)


def courseList(request):
    if request.user.is_authenticated:
        response = CourseService.get_all_courses()
        data = {
            'courses': response
        }

        return render(request, 'administration/courseAdm/courseList.html', data)
    elif not request.user.is_authenticated:
        messages.error(
            request, 'Usuário ou Senha incorretos, efetue o login novamente')
        return redirect('login')


def courseRegistration(request):
    if request.user.is_authenticated:
        template = 'administration/courseAdm/courseRegistration.html'

        if request.method == 'POST':
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            if token == None:
                messages.error(
                    request, 'Sessão Finalizada, por favor efetue o login novamente')
                return redirect('login')
            else:
                messages.success(request, 'Cadastrado com sucesso')
                CourseService.post_courses(request.POST, request.FILES, token)
                template = 'administration/courseAdm/courseList.html'

        course = CourseService.get_all_courses()
        data = {
            'courses': course
        }
        return render(request, template, data)
    elif not request.user.is_authenticated:
        messages.error(
            request, 'Usuário ou Senha incorretos, efetue o login novamente')
        return redirect('login')


def courseSave(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            CourseService.post_courses(request.POST, request.FILES)
            course = CourseService.get_courses()

        data = {
            'courses': course
        }
        return render(request, 'administration/courseAdm/courseList.html', data)
    elif not request.user.is_authenticated:
        messages.error(
            request, 'Usuário ou Senha incorretos, efetue o login novamente')
        return redirect('login')


def courseMaintenance(request, course_id):
    if request.user.is_authenticated:
        template = 'administration/courseAdm/courseMaintenance.html'
        course = CourseService.get_courses_by_id(course_id)
        if request.method == 'POST':
            template = 'administration/courseAdm/courseList.html'
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            CourseService.put_courses(
                request.POST, request.FILES, course_id, token)
            course = CourseService.get_all_courses()

        data = {
            'courses': course,
        }
        return render(request, template, data)
    else:
        return redirect('login')


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
        return render(request, 'administration/courseAdm/courseDetails.html', data)
    else:
        return redirect('login')
