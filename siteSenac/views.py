from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
from siteSenac.send_email import Send_EmailService
from university.service import UniversityService
from .service import *

_USERNAME = '' 
_PASSWORD= ''

def index(request):
    return render(request, 'userPages/homeSenac.html')

def services(request):
    return render(request, 'userPages/services.html')

def modalities(request):
    return render(request, 'userPages/modalities.html')

def contact(request):
    if request.method == 'POST':
        if request.POST['universities'] != '0':
            Send_EmailService.post_send_email(request.POST)
            messages.success(request, 'E-mail enviado com sucesso')

    response = UniversityService.get_universities()

    data = {
        'universities': response
    }
    return render(request, 'userPages/contact.html', data)

def administration_home(request):
    if request.user.is_authenticated:
        template = 'administration/homeAdministration.html'
    else:
        template = 'userPages/login.html'
    return render(request, template)

def login(request):
    return render(request, 'userPages/login.html')

def administration(request):
    global _USERNAME, _PASSWORD
    template = 'userPages/login.html'
    if request.method == 'POST':   
        if User.objects.filter(username=request.POST['username']).exists():
            user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                _USERNAME = request.POST['username']
                _PASSWORD = request.POST['password']
            if request.user.is_authenticated:
                template = 'administration/homeAdministration.html'
            elif not request.user.is_authenticated:
                messages.error(request, 'Usuário ou Senha incorretos, efetue o login novamente')
                return redirect('login')
            
    return render(request, template)

def get_user_pass():
    list = [_USERNAME, _PASSWORD]
    return list
            

def logout(request):
    auth.logout(request)
    return redirect('index')





    
