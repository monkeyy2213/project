from typing import Any
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

class AnimalHome(DataMixin, ListView):
    model = Patient
    template_name = 'animals/index.html' 
    context_object_name = 'patients'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

def about(request):
    return render(request, 'animals/about.html', {'menu': menu, 'title': 'О сайте'})

class AddAnimals(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddAnimalForm
    template_name = 'animals/add_animals.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление животного")
        return dict(list(context.items()) + list(c_def.items()))

def contact(request):
    return render(request, 'animals/contact.html', {'menu': menu, 'title': 'Контакты'})

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'animals/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'animals/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

# def profile(request):
#     return render(request, 'animals/profile.html', {'menu': menu, 'title': 'Профиль'})

# def addanimals(request):
#     if request.method == 'POST':
#         form = AddAnimalForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')

#     else:
#         form = AddAnimalForm()
#     return render(request, 'animals/add_animals.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

# def login(request):
#     return HttpResponse("Авторизация")

# def index(request):
#     patients = Patient.objects.all()
#     context = {
#         'patients': patients,
#         'menu': menu,
#         'title': 'Главная страница'
#     }
#     return render(request, 'animals/index.html', context=context)