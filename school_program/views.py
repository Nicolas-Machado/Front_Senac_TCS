from django.contrib import messages
from django.shortcuts import redirect, render
from school_program.service import School_ProgramService
from subject.service import SubjectService
from course.service import CourseService

from siteSenac.views import get_user_pass, token_login

def post_school_program(request, course_id):
    token = token_login(request)
    if(token == None):
        return redirect('login')
    status = School_ProgramService.post_School_Program(request.POST, course_id, token)
    if(status.status_code == 201):
        messages.success(request, 'Fase Cadastrada Com Sucesso')
    else :
        messages.error(request, 'Falha ao Cadastrar Fase')
    
    course = CourseService.get_courses_by_id(course_id)
    phases = CourseService.get_phases_in_courses(course_id)
    data = {
        'courses': course,
        'phases': phases,
    }
    return render(request, 'administration/courseAdm/courseDetails.html', data)

def schoolProgramRegistration(request, course_id):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            post_school_program(request, course_id)

        course = CourseService.get_courses_by_id(course_id)
        subjects = SubjectService.get_subjects()
    
        data = {
        "subjects" : subjects,
        "courses" : course
        }

        return render(request, 'administration/schoolProgramAdm/schoolProgramRegistration.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')

def put_school_program(request, phases_id, phases):
    token = token_login(request)
    if(token == None):
        return redirect('login')

    course_id = phases['courses']    
    status = School_ProgramService.put_School_Program(request, phases_id, course_id, token)
    if(status.status_code == 200):
        messages.success(request, 'Salvo Com Sucesso')
    else :
        messages.error(request, 'Falha ao Salvar')
    course = CourseService.get_courses_by_id(course_id)
    phases = CourseService.get_phases_in_courses(course_id)
    data = {
        'courses': course,
        'phases': phases,
    }
    return render(request, 'administration/courseAdm/courseDetails.html', data)

def schoolProgramMaintenance(request, phases_id):
    if request.user.is_authenticated:
        phases = School_ProgramService.get_school_program_by_id(phases_id)

        if request.method == 'POST':
            put_school_program(request.POST, phases_id, phases)
            
        school_program = School_ProgramService.get_subjects_in_school_program(phases_id)
        subjects = SubjectService.get_subjects()
        phases_sub = []

        for subject in subjects:
            phases_sub.append(subject)

        for schoolProgram in school_program:
            for subject in subjects:
                if schoolProgram['id'] == subject['id']:
                    phases_sub.remove(schoolProgram)
    
        data = {
        "phases" : phases,
        "phases_sub" : phases_sub,
        "subjects" : school_program
        }

        return render(request, 'administration/schoolProgramAdm/schoolProgramMaintenance.html', data)


    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')
    
def school_ProgramDelete(request, school_program_id):
    if request.user.is_authenticated:
        token = token_login(request)
        if(token == None):
            return redirect('login')
        phases = School_ProgramService.get_school_program_by_id(school_program_id)
        course_id = phases['courses']
        status = School_ProgramService.delete_school_program(school_program_id, token)
        if(status.status_code == 204):
            messages.success(request, 'Fase Deletada Com Sucesso')
        else :
            messages.error(request, 'Falha ao Deletar Fase')

        course = CourseService.get_courses_by_id(course_id)
        phases = CourseService.get_phases_in_courses(course_id)
        data = {
            'courses': course,
            'phases': phases,
        }
        return render(request, 'administration/courseAdm/courseDetails.html', data)
    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')
