from django.shortcuts import redirect, render
from course.service import CourseService
from enrollment.service import EnrollmentService
from siteSenac.service import adm_authenticate
from siteSenac.views import get_user_pass
from datetime import datetime
from university.service import UniversityService


def data_enrollment_list():
    response = EnrollmentService.get_enrollments()
    date_now = datetime.today().strftime('%Y-%m-%d')


    data = {
        'enrollments': response,
        'date_now' : date_now
    }
    return data

def enrollmentList(request):

    if request.user.is_authenticated:
        data = data_enrollment_list()
        
        return render(request, 'administration/enrollmentAdm/enrollmentList.html', data)
    else:
        return redirect('login')
    

def post_enrollment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            EnrollmentService.post_enrollment(request.POST, token)
            data = data_enrollment_list()            
            return render(request, 'administration/enrollmentAdm/enrollmentList.html', data)
    else:
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
    else:
        return redirect('login')

def enrollmentMaintenance(request):
    if request.user.is_authenticated:
        course = CourseService.get_all_courses()
        university = UniversityService.get_all_universities()

        data = {
            'courses': course,
            'universities': university
        }
        return render(request, 'administration/enrollmentAdm/enrollmentMaintenance.html', data) 
    else:
        return redirect('login')

def enrollment_select(request):
    if request.user.is_authenticated:
        courses = CourseService.get_courses_in_university(request.GET['university'])

        data = {
            'courses_enrollment' : courses
        }

        return render(request, 'partials/enrollmentPartials/_enrollments_results.html', data)
    else:
        return redirect('login')
