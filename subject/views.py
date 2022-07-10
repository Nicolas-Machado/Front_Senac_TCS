from django.shortcuts import redirect, render
from siteSenac.service import adm_authenticate
from django.contrib import messages
from siteSenac.views import get_user_pass, token_login
from subject.service import SubjectService


def post_subject(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            token = token_login(request)
            if(token == None):
                return redirect('login')
            status = SubjectService.post_subject(request.POST, token)
            if(status.status_code == 201):
                messages.success(request, 'Matéria Cadastrada Com Sucesso')
            else:
                messages.error(request, 'Falha ao Cadastrar Matéria')

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

def put_subject(request, subject_id):
    token = token_login(request)
    if(token == None):
        return redirect('login')
    status = SubjectService.put_subject(request.POST, subject_id, token)
    if(status.status_code == 200):
        messages.success(request, 'Salvo com sucesso')
    else:
        messages.error(request, 'Falha ao Salvar')
    subjects = SubjectService.get_subjects()
        
    data = {
        "subjects": subjects
    }
    return render(request, 'administration/subjectAdm/subjectList.html', data)

def subjectMaintenance(request, subject_id):
    if request.user.is_authenticated:

        if request.method == 'POST':
            return put_subject(request, subject_id)

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
        token = token_login(request)
        if(token == None):
            return redirect('login')
        status = SubjectService.delete_subject(subject_id, token)
        if(status.status_code == 204):
            messages.success(request, 'Matéria Deletada Com Sucesso')
        else:
            messages.error(request, 'Falha ao Deletar Matéria')
        subjects = SubjectService.get_subjects()

        data = {
            "subjects": subjects
        }

        return render(request, 'administration/subjectAdm/subjectList.html', data)

    elif not request.user.is_authenticated:
        messages.error(
            request, 'Sessão Finalizada, por favor efetue o login novamente')
        return redirect('login')


