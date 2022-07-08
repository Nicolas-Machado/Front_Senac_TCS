from django.shortcuts import redirect, render
from school_program.service import School_ProgramService
from subject.service import SubjectService
from siteSenac.service import adm_authenticate
from course.service import CourseService

from siteSenac.views import get_user_pass

def schoolProgramRegistration(request, course_id):
    if request.user.is_authenticated:
        course = CourseService.get_courses_by_id(course_id)
        subjects = SubjectService.get_subjects()
    
        data = {
        "subjects" : subjects,
        "courses" : course
        }

        if request.method == 'POST':
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            School_ProgramService.post_School_Program(request.POST, course_id, token)
            
            phases = CourseService.get_phases_in_courses(course_id)
            # subjects = CourseService.get_subjects_in_phases()
            data = {
                'courses': course,
                'phases': phases,
                # 'subjects': subjects
            }
            return render(request, 'administration/courseAdm/courseDetails.html', data)
        return render(request, 'administration/schoolProgramAdm/schoolProgramRegistration.html', data)
    else:
        return redirect('login')

def schoolProgramMaintenance(request, phases_id):
    if request.user.is_authenticated:
        phases = School_ProgramService.get_school_program_by_id(phases_id)

        if request.method == 'POST':
            list = get_user_pass()
            course_id = phases['courses']
            token = adm_authenticate(list[0], list[1])
            School_ProgramService.put_School_Program(request.POST, phases_id, course_id, token)
            course = CourseService.get_courses_by_id(course_id)
            phases = CourseService.get_phases_in_courses(course_id)
            # subjects = CourseService.get_subjects_in_phases()
            data = {
                'courses': course,
                'phases': phases,
                # 'subjects': subjects
            }
            return render(request, 'administration/courseAdm/courseDetails.html', data)
            
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


    else:
        return redirect('login')

def school_ProgramDelete(request, school_program_id):
    if request.user.is_authenticated:
        list = get_user_pass()
        token = adm_authenticate(list[0], list[1])
        phases = School_ProgramService.get_school_program_by_id(school_program_id)
        course_id = phases['courses']
        School_ProgramService.delete_school_program(school_program_id, token)

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
