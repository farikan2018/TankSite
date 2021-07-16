from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import TankForm, RegisterForm, LoginForm, KlasForm, StranaForm
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth import login, logout
from django.contrib import messages


class HomeTank(ListView):
    model = Tank
    template_name = 'firstapp/index.html'
    context_object_name = 'tanks'
    paginate_by = 5

    def get_queryset(self):
        return Tank.objects.filter(publish=True)


class GetStrana(ListView):
    model = Tank
    template_name = 'firstapp/strana_sort.html'
    context_object_name = 'tanks'
    paginate_by = 5

    def get_queryset(self):
        return Tank.objects.filter(strana_id=self.kwargs['strana_id'], publish=True)


class GetKlas(ListView):
    model = Tank
    template_name = 'firstapp/klas_sort.html'
    context_object_name = 'tanks'
    paginate_by = 5

    def get_queryset(self):
        return Tank.objects.filter(klas_id=self.kwargs['klas_id'], publish=True)


class About(ListView):
    model = Tank
    template_name = 'firstapp/about.html'


class CreateForm(CreateView):
    form_class = TankForm
    template_name = 'firstapp/create.html'
    success_url = '/'


class Proba(ListView):
    model = Tank
    template_name = 'firstapp/proba.html'
    context_object_name = 'tanks'

    def get_queryset(self):
        return Tank.objects.filter(publish=True)


def create(request):
    if request.method == 'POST':
        form = TankForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно предложена. Она появиться в скором времени после проверки модератора')
            return redirect('home')
        else:
            messages.error(request, 'Форма была неверной 1')

    if request.method == 'POST':
        strana = StranaForm(request.POST)
        if strana.is_valid():
            strana.save()
            messages.success(request, 'Страна успешно предложена. Она появиться в скором времени после проверки модератора')
            return redirect('create')
        else:
            messages.error(request, 'Форма была неверной 2')

    if request.method == 'POST':
        klas = KlasForm(request.POST)
        if klas.is_valid():
            klas.save()
            messages.success(request, 'Клас техники успешно предложена. Она появиться в скором времени после проверки модератора')
            return redirect('create')
        else:
            messages.error(request, 'Форма была неверной 3')

    strana = StranaForm
    form = TankForm
    klas = KlasForm
    elements = {
        "form": form,
        "strana": strana,
        "klas": klas,
    }
    return render(request, 'firstapp/create.html', elements)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Проблема при регистрации')
    else:
        form = RegisterForm()
    return render(request, 'firstapp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'firstapp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')