from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.models import User, Group

# Create your views here.

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/reg.html'
    success_url = '/login'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/log.html'
    def get_success_url(self):
        return '/news'


@login_required
def logout_user(request):
    logout(request)
    return redirect('log')


@login_required
def profile(request):
    data = ''
    if request.user.is_superuser:
        data = 'Администратор'
    elif request.user.groups.filter(name='Модератор'):
        data = 'Модератор'
    else:
        data = 'Простой пользователь'
    return render(request, 'main/profile.html', {'role': data})


def contacts(request):
    return render(request, 'main/contacts.html')


def gallery(request):
    return render(request, 'main/gallery.html')


def confpolicy(request):
    return render(request, 'main/confpolicy.html')


def swyaz(request):
    return render(request, 'main/swyaz.html')


def admpanel(request):
    all_users = User.objects.values()
    if request.method == 'POST':
        user_id = ''.join(request.POST.getlist('chk[]'))
        user = User.objects.get(id=user_id)
        roles = Group.objects.filter(user=user)
        if Group.objects.filter(name="Модератор").first() in roles:
            user.groups.clear()
            user.is_staff = False
            user.save()
        else:
            user.groups.add('1')
            user.is_staff = True
            user.save()
    return render(request, 'main/adminpanel.html', {'all_users': all_users})