from django.shortcuts import redirect, render
from course.service import CourseService
from course.views import courses_results_request
from siteSenac.send_email import Send_EmailService
from siteSenac.service import *
from siteSenac.views import get_user_pass
from university.service import UniversityService


def universities(request):
    template = ''
    if 'search' in request.GET:
        name = request.GET['search']
        response = UniversityService.get_universities_by_name(name)
        template = 'partials/_universities_results.html'
    else:
        response = UniversityService.get_universities()
        template = 'userPages/universityUser/universities.html'
    data = {
        'universities': response
    }
    return render(request, template, data)

def university(request, university_id):
    if request.method == 'POST':
        Send_EmailService.post_send_email(request.POST)

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
        template = 'administration/universityAdm/universityList.html'
    
        if 'id' in request.POST:
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            UniversityService.put_active_universities(request.POST['id'], token)
            template = 'partials/_admUniversity_check_results.html'

        response = UniversityService.get_all_universities()
        data = {
            'universities': response
        }
    else:
        return redirect('login')
    
    return render(request, template, data)


def post_university(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
                list = get_user_pass()
                token = adm_authenticate(list[0], list[1])
                UniversityService.post_university(request.POST, request.FILES, token)
                response = UniversityService.get_all_universities()
                data = {
                'universities': response
                }
                return render(request, 'administration/universityAdm/universityList.html', data)
    else:
        return redirect('login')

def universityRegistration(request):
    if request.user.is_authenticated:
        response = CourseService.get_all_courses()
        data = {
            'courses': response
        }

        return render(request, 'administration/universityAdm/universityRegistration.html', data)
    else:
        return redirect('login')

def put_university(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            UniversityService.put_university(request.POST, request.FILES, token)
            response = UniversityService.get_all_universities()
            data = {
            'universities': response
            }

            return render(request, 'administration/universityAdm/universityList.html', data)
    else:
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
                    courses_reg.remove(courses_)
        
        data = {
            'universities': university,
            'courses': courses_reg,
            'courses_uni': courses_uni
        }

        return render(request, 'administration/universityAdm/universityMaintenance.html', data)
        
    else:
        return redirect('login')