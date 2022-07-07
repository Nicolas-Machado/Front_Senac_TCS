from django.shortcuts import redirect, render
from course.service import *
from enrollment.service import EnrollmentService
from university.service import *

def enrollmentList(request):

    if request.user.is_authenticated:
        template = 'administration/enrollmentAdm/enrollmentList.html'

        response = EnrollmentService.get_enrollments()

        data = {
            'enrollments': response
        }

    else:
        return redirect('login')
    
    return render(request, template, data)

def enrollmentRegistration(request):
    course = CourseService.get_all_courses()
    university = UniversityService.get_all_universities()

    data = {
        'courses': course,
        'universities': university
    }
    return render(request, 'administration/enrollmentAdm/enrollmentRegistration.html', data)

def enrollmentMaintenance(request):
    course = CourseService.get_all_courses()
    university = UniversityService.get_all_universities()

    data = {
        'courses': course,
        'universities': university
    }
    return render(request, 'administration/enrollmentAdm/enrollmentMaintenance.html', data)