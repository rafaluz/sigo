from django.shortcuts import render, get_object_or_404
from .models import *    
from django.urls import reverse_lazy, reverse    
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin    
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect 
from .forms import TimeTableCreateForm
# Create your views here.

############### Turno ###############
class ClassShiftCreate(CreateView, ListView):
    model = ClassShift
    template_name = 'class_shift/class_shift_add.html'
    fields = '__all__'

    def get_success_url(self):
        # enviando mensagem de sucesso
        messages.add_message(self.request, messages.SUCCESS, "Turno Cadastrado com sucesso!")
        return reverse('school:class_shift_create')

class ClassShiftUpdate(UpdateView, ListView):
    model = ClassShift
    template_name = 'class_shift/class_shift_edit.html'
    fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Turno Alterado com sucesso!")
        return reverse('school:class_shift_create')

class ClassShiftDelete(DeleteView):
    model = ClassShift
    template_name = 'class_shift/class_shift_confirm_delete.html'
    # success_url = reverse_lazy('accounts:class_shift_create')
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Turno Removido com sucesso!")
        return reverse('school:class_shift_create')


############### Horarios das aulas em cada turno ###############
class TimeTableCreate(CreateView, ListView):
    model = TimeTable
    template_name = 'time_table/time_table_add.html'
    form_class = TimeTableCreateForm
    # fields = ['start']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # pegar a chave do turno que passei pela url
        class_shift_pk = self.kwargs['class_shift_pk']
        # pegar o turno
        class_shift = get_object_or_404(ClassShift, pk=class_shift_pk)
        time_tables = TimeTable.objects.filter(class_shift = class_shift_pk)

        context.update({
            'class_shift':class_shift,
			'object_list': time_tables,
		    })

        return context

    def form_valid(self, form):
        time_table = form.save(commit=False)
        
        
        class_shift_pk = self.kwargs['class_shift_pk'] # pegar a chave do turno que passei pela url
        class_shift = get_object_or_404(ClassShift, pk=class_shift_pk) # pegar o turno

        time_table.class_shift = class_shift
        time_table.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # enviando mensagem de sucesso
        messages.add_message(self.request, messages.SUCCESS, "Horário Cadastrado com sucesso!")
        # Enviar novamente a pk do turno correspondente para a pagina de criação de horarios
        return reverse('school:time_table_create', kwargs={'class_shift_pk': self.kwargs['class_shift_pk']})
   
class TimeTableUpdate(UpdateView, ListView):
    model = TimeTable
    template_name = 'time_table/time_table_edit.html'
    form_class = TimeTableCreateForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # pegar a chave do turno que passei pela url
        class_shift_pk = self.kwargs['class_shift_pk']
        # pegar o turno
        class_shift = get_object_or_404(ClassShift, pk=class_shift_pk)
        time_tables = TimeTable.objects.filter(class_shift = class_shift_pk)

        context.update({
            'class_shift':class_shift,
			'object_list': time_tables,
		    })

        return context

    def form_valid(self, form):
        time_table = form.save(commit=False)
        
        
        class_shift_pk = self.kwargs['class_shift_pk'] # pegar a chave do turno que passei pela url
        class_shift = get_object_or_404(ClassShift, pk=class_shift_pk) # pegar o turno

        time_table.class_shift = class_shift
        time_table.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # enviando mensagem de sucesso
        messages.add_message(self.request, messages.SUCCESS, "Horário Cadastrado com sucesso!")
        # Enviar novamente a pk do turno correspondente para a pagina de criação de horarios
        return reverse('school:time_table_create', kwargs={'class_shift_pk': self.kwargs['class_shift_pk']})

class TimeTableDelete(DeleteView):
    model = TimeTable
    template_name = 'time_table/time_table_confirm_delete.html'
    # success_url = reverse_lazy('accounts:time_table_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # pegar a chave do turno que passei pela url
        class_shift_pk = self.kwargs['class_shift_pk']
        # pegar o turno
        class_shift = get_object_or_404(ClassShift, pk=class_shift_pk)

        context.update({
            'class_shift':class_shift,
		})

        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Horário Removido com sucesso!")
        return reverse('school:time_table_create', kwargs={'class_shift_pk': self.kwargs['class_shift_pk']})