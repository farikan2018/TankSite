from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select, ClearableFileInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=(TextInput({"class": "form-control", "placeholder": "Введите ник пользователя"})))
    password = forms.CharField(label='', widget=(TextInput({"class": "form-control", "placeholder": "Введите пароль"})))
    # captcha = CaptchaField(label='Введите каптчу')


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=(TextInput({"class": "form-control", "placeholder": "Введите ник пользователя"})))
    email = forms.EmailField(label='', widget=(EmailInput({"class": "form-control", "placeholder": "Введите ваш email"})))
    password1 = forms.CharField(label='', widget=(TextInput({"class": "form-control", "placeholder": "Введите пароль"})))
    password2 = forms.CharField(label='', widget=(TextInput({"class": "form-control", "placeholder": "Повторите пароль"})))
    # captcha = CaptchaField(label='Введите каптчу')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TankForm(ModelForm):
    class Meta:
        model = Tank
        fields = ['title', 'opis', 'strana', 'klas', 'photo', 'silka',]
        widgets = {
            'title': TextInput({
                "class": "form-control",
                "placeholder": "Введите название"
            }),
            'opis': Textarea({
                "class": "form-control",
                "placeholder": "Введите описание"
            }),
            'strana': Select({
                "class": "form-control"
            }),
            'klas': Select({
                "class": "form-control"
            }),
            'photo': ClearableFileInput({
                "class": "form-control",
            }),
            'silka': TextInput({
                "class": "form-control",
                "placeholder": "Введите ссылку",
            }),
        }


class StranaForm(ModelForm):
    class Meta:
        model = Strana
        fields = ['title', ]
        widgets = {
            'title': TextInput({
                "class": "form-control",
                "placeholder": "Введите название страны"
            })}


class KlasForm(ModelForm):
    class Meta:
        model = Klas
        fields = ['title', ]
        widgets = {
            'title': TextInput({
                "class": "form-control",
                "placeholder": "Введите название класса"
            })}