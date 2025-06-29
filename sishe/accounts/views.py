from django.shortcuts import render
from .models import *    
from sishe.accounts.forms import CreateUserForm    
from django.urls import reverse_lazy, reverse    
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin    
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q

from dal import autocomplete

class UserCreate(CreateView, ListView):
    model = User
    template_name = 'user/user_add.html'
    form_class = CreateUserForm
    # success_url = reverse_lazy('accounts:login')
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Coordenador criado com sucesso!")
        return reverse('accounts:user_create')

class UserUpdate(UpdateView, ListView):
    model = User
    template_name = 'user/user_edit.html'
    form_class = CreateUserForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Coordenador alterado com sucesso!")
        return reverse('accounts:user_create')



class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs



############### Axis ###############
class AxisCreate(CreateView, ListView):
    model = Axis
    template_name = 'axis/axis_add.html'
    fields = ['name']

    def get_success_url(self):
        # enviando mensagem de sucesso
        messages.add_message(self.request, messages.SUCCESS, "Eixo Cadastrado com sucesso!")
        return reverse('accounts:axis_create')

class AxisUpdate(UpdateView, ListView):
    model = Axis
    template_name = 'axis/axis_edit.html'
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Eixo Alterado com sucesso!")
        return reverse('accounts:axis_create')

class AxisDelete(DeleteView):
    model = Axis
    template_name = 'axis/axis_confirm_delete.html'
    # success_url = reverse_lazy('accounts:axis_create')
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Eixo Removido com sucesso!")
        return reverse('accounts:axis_create')


############### Teacher ###############
class TeacherCreate(CreateView, ListView):
    model = Teacher
    template_name = 'teacher/teacher_add.html'
    fields = '__all__'
    # fields = ['name']

    def get_success_url(self):
        # enviando mensagem de sucesso
        messages.add_message(self.request, messages.SUCCESS, "Professor Cadastrado com sucesso!")
        return reverse('accounts:teacher_create')

class TeacherUpdate(UpdateView, ListView):
    model = Teacher
    template_name = 'teacher/teacher_edit.html'
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Professor Alterado com sucesso!")
        return reverse('accounts:teacher_create')

class TeacherDelete(DeleteView):
    model = Teacher
    template_name = 'teacher/teacher_confirm_delete.html'
    # success_url = reverse_lazy('accounts:teacher_create')
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Professor Removido com sucesso!")
        return reverse('accounts:teacher_create')

class TeacherAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Teacher.objects.all()
        if self.q:
            qs = qs.filter(Q(name__icontains=self.q) | Q(axis__name__icontains=self.q))
        return qs