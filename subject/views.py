from ast import Sub
from django.shortcuts import redirect, render
from siteSenac.service import adm_authenticate
from django.contrib import messages
from siteSenac.views import get_user_pass
from subject.service import SubjectService


def post_subject(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            if token == None:
                messages.error(
                    request, 'Sessão Finalizada, por favor efetue o login novamente')
                return redirect('login')
            else:
                messages.success(request, 'Salvo com sucesso')
                SubjectService.post_subject(request.POST, token)

                subjects = SubjectService.get_subjects()

            data = {
                "subjects": subjects
            }
            return render(request, 'administration/subjectAdm/subjectList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def subjectRegistration(request):
    if request.user.is_authenticated:
        return render(request, 'administration/subjectAdm/subjectRegistration.html')
    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def subjectMaintenance(request, subject_id):
    if request.user.is_authenticated:

        if request.method == 'POST':
            list = get_user_pass()
            token = adm_authenticate(list[0], list[1])
            if token == None:
                messages.error(
                    request, 'Sessão Finalizada, por favor efetue o login novamente')
                return redirect('login')
            else:
                messages.success(request, 'Salvo com sucesso')
                SubjectService.put_subject(request.POST, subject_id, token)
                subjects = SubjectService.get_subjects()
                
            data = {
                "subjects": subjects
            }
            return render(request, 'administration/subjectAdm/subjectList.html', data)

        subjects = SubjectService.get_subject_by_id(subject_id)

        data = {
            "subjects": subjects
        }
        return render(request, 'administration/subjectAdm/subjectMaintenance.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def subjectList(request):
    if request.user.is_authenticated:
        subjects = SubjectService.get_subjects()

        data = {
            "subjects": subjects
        }

        return render(request, 'administration/subjectAdm/subjectList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


def subjectDelete(request, subject_id):
    if request.user.is_authenticated:
        list = get_user_pass()
        token = adm_authenticate(list[0], list[1])
        if token == None:
            messages.error(
                request, 'Sessão Finalizada, por favor efetue o login novamente')
            return redirect('login')
        else:
            messages.success(request, 'Deletado com sucesso')
            SubjectService.delete_subject(subject_id, token)
            subjects = SubjectService.get_subjects()

        data = {
            "subjects": subjects
        }

        return render(request, 'administration/subjectAdm/subjectList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')
