from django.shortcuts import redirect, render
from course.service import CourseService
from enrollment.service import EnrollmentService
from siteSenac.views import token_login
from datetime import datetime
from university.service import UniversityService
from django.contrib import messages


def data_enrollment_list():
    response = EnrollmentService.get_enrollments()
    date_now = datetime.today().strftime('%Y-%m-%d')

    data = {
        'enrollments': response,
        'date_now': date_now
    }
    return data


def enrollmentList(request):

    if request.user.is_authenticated:
        data = data_enrollment_list()

        return render(request, 'administration/enrollmentAdm/enrollmentList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def post_enrollment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            token = token_login(request)
            if(token == None):
                 return redirect('login')
            messages.success(request, 'Salvo com sucesso')
            EnrollmentService.post_enrollment(request.POST, token)
            data = data_enrollment_list()
            return render(request, 'administration/enrollmentAdm/enrollmentList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def enrollmentRegistration(request):
    if request.user.is_authenticated:
        course = CourseService.get_all_courses()
        university = UniversityService.get_all_universities()

        data = {
            'courses': course,
            'universities': university
        }
        return render(request, 'administration/enrollmentAdm/enrollmentRegistration.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def enrollment_select(request):
    if request.user.is_authenticated:
        courses = CourseService.get_courses_in_university(
            request.GET['university'])

        data = {
            'courses_enrollment': courses
        }

        return render(request, 'partials/enrollmentPartials/_enrollments_results.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')
    
def delete_enrollment(request, enrollment_id):
    if request.user.is_authenticated:
        token = token_login(request)
        if(token == None):
            return redirect('login')
            
        status = EnrollmentService.delete_enrollment(enrollment_id, token)
        if(status.status_code == 204):
            messages.success(request, 'Inscrição Deletada Com Sucesso')
        else :
            messages.error(request, 'Falha ao Deletar Inscrição')
        
        data = data_enrollment_list()

        return render(request, 'administration/enrollmentAdm/enrollmentList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')
