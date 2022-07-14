from django.shortcuts import redirect, render
from course.service import CourseService
from enrollment.service import EnrollmentService
from siteSenac.send_email import Send_EmailService
from siteSenac.service import *
from siteSenac.views import token_login
from django.contrib import messages
from datetime import datetime

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
    if occupation_area != 'Área de atuação':
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
            status = Send_EmailService.post_send_email(request.POST)
            if(status.status_code == 201):
                messages.success(request, 'E-mail Enviado Com Sucesso')
            else:
                messages.error(request, 'Falha ao Enviar E-mail')

    course = CourseService.get_courses_by_id(course_id)
    university = CourseService.get_universities_in_course(course_id)
    phases = CourseService.get_phases_in_courses(course_id)
    enrollment = EnrollmentService.get_enrollments_in_course(course_id)
    enrollments = []

    for enrollment in enrollment:
        for universities in university:
            if enrollment['universities'] == universities['name']:
                if enrollment['date_final'] > datetime.today().strftime('%Y-%m-%d'):
                    enrollment['date_final'] = datetime.strptime(enrollment['date_final'], '%Y-%m-%d').strftime('%d/%m/%y')
                    enrollment['date_initial'] = datetime.strptime(enrollment['date_initial'], '%Y-%m-%d').strftime('%d/%m/%y')
                    enrollments.append(enrollment)
                    break

    data = {
        'universities': university,
        'courses': course,
        'phases': phases,
        'enrollments' : enrollments
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
            token = token_login(request)
            if(token == None):
                 return redirect('login')
            status = CourseService.post_courses(request.POST, request.FILES, token)
            if(status.status_code == 201):
                messages.success(request, 'Curso Cadastrado Com Sucesso')
            else:
                messages.error(request, 'Falha ao Cadastrar Curso')
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


def courseMaintenance(request, course_id):
    if request.user.is_authenticated:
        template = 'administration/courseAdm/courseMaintenance.html'
        course = CourseService.get_courses_by_id(course_id)
        if request.method == 'POST':
            token = token_login(request)
            if(token == None):
                 return redirect('login')

            status = CourseService.put_courses(
                request.POST, request.FILES, course_id, token)
            if(status.status_code == 200):
                messages.success(request, 'Salvo Com Sucesso')
            else:
                messages.error(request, 'Falha ao Salvar')

            course = CourseService.get_all_courses()
            template = 'administration/courseAdm/courseList.html'

        data = {
            'courses': course,
        }
        return render(request, template, data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Usuário ou Senha incorretos, efetue o login novamente')
        return redirect('login')


def courseDetails(request, course_id):
    if request.user.is_authenticated:
        course = CourseService.get_courses_by_id(course_id)
        phases = CourseService.get_phases_in_courses(course_id)


        data = {
            'courses': course,
            'phases': phases,
        }
        
        return render(request, 'administration/courseAdm/courseDetails.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Usuário ou Senha incorretos, efetue o login novamente')
        return redirect('login')
