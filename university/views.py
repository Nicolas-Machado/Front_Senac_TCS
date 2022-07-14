from django.shortcuts import redirect, render
from course.service import CourseService
from course.views import courses_results_request
from siteSenac.send_email import Send_EmailService
from siteSenac.service import *
from siteSenac.views import get_user_pass, token_login
from university.service import UniversityService
from django.contrib import messages


def universities(request):
    template = ''
    if 'search' in request.GET:
        name = request.GET['search']
        response = UniversityService.get_universities_by_name(name)
        template = 'partials/universityPartials/_universities_results.html'
    else:
        response = UniversityService.get_universities()
        template = 'userPages/universityUser/universities.html'
    data = {
        'universities': response
    }
    return render(request, template, data)


def university(request, university_id):
    if request.method == 'POST':
        status = Send_EmailService.post_send_email(request.POST)
        if(status.status_code == 201):
            messages.success(request, 'E-mail Enviado Com Sucesso')
        else:
            messages.error(request, 'Falha ao Enviar E-mail')

    university = UniversityService.get_universities_by_id(university_id)
    course = CourseService.get_courses_in_university(university_id)
    courses_results_request(course, 'university_course', university)
    data = {
        'universities': university,
        'courses': course
    }
    return render(request, 'userPages/universityUser/university.html', data)


def universityList(request):
    if request.user.is_authenticated:

        response = UniversityService.get_all_universities()
        data = {
            'universities': response
        }
        return render(request, 'administration/universityAdm/universityList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def post_university(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            token = token_login(request)
            if(token == None):
                 return redirect('login')
            status = UniversityService.post_university(
            request.POST, request.FILES, token)
            if(status.status_code == 201):
                messages.success(request, 'Unidade Cadastrada Com Sucesso')
            else:
                messages.error(request, 'Falha ao Cadastrar Unidade')
            response = UniversityService.get_all_universities()
            data = {
                'universities': response
            }
            return render(request, 'administration/universityAdm/universityList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def universityRegistration(request):
    if request.user.is_authenticated:
        response = CourseService.get_all_courses()
        data = {
            'courses': response
        }

        return render(request, 'administration/universityAdm/universityRegistration.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def put_university(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            token = token_login(request)
            if(token == None):
                return redirect('login')
            status = UniversityService.put_university(
                request.POST, request.FILES, token)
            if(status.status_code == 200):
                messages.success(request, 'Salvo com sucesso')
            else:
                messages.error(request, 'Falha ao Salvar')
            response = UniversityService.get_all_universities()
            
            data = {
                'universities': response
            }
            return render(request, 'administration/universityAdm/universityList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def universityMaintenance(request, university_id):
    if request.user.is_authenticated:
        university = UniversityService.get_universities_by_id(university_id)
        course = CourseService.get_courses()
        courses_uni = CourseService.get_courses_in_university(university_id)
        courses_reg = []

        for courses in course:
            courses_reg.append(courses)

        for courses_ in courses_uni:
            for courses in course:
                if courses_['id'] == courses['id']:
                    courses_reg.remove(courses)

        data = {
            'universities': university,
            'courses': courses_reg,
            'courses_uni': courses_uni
        }

        return render(request, 'administration/universityAdm/universityMaintenance.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')
