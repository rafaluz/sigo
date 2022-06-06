import json
from django.shortcuts import render, get_object_or_404
from .models import *    
from django.urls import reverse_lazy, reverse    
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin    
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse 
from .forms import TimeTableCreateForm, CourseForm, SemesterForm, GradeForm, CurricularComponentForm
from dal import autocomplete
from django.db.models import Q
import random
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




############### Curso ###############
class CourseCreate(CreateView, ListView):
    model = Course
    template_name = 'course/course_add.html'
    form_class = CourseForm
    # fields = '__all__'

    def get_success_url(self):
        # enviando mensagem de sucesso
        messages.add_message(self.request, messages.SUCCESS, "Curso Cadastrado com sucesso!")
        return reverse('school:course_create')

class CourseUpdate(UpdateView, ListView):
    model = Course
    template_name = 'course/course_edit.html'
    form_class = CourseForm
    # fields = '__all__'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Curso Alterado com sucesso!")
        return reverse('school:course_create')

class CourseDelete(DeleteView):
    model = Course
    template_name = 'course/course_confirm_delete.html'
    # success_url = reverse_lazy('accounts:course_create')
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Curso Removido com sucesso!")
        return reverse('school:course_create')

class CourseAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Course.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

############### Periodo Letivo ###############
class SemesterCreate(CreateView, ListView):
    model = Semester
    template_name = 'semester/semester_add.html'
    form_class = SemesterForm

    def get_success_url(self):
        # enviando mensagem de sucesso
        messages.add_message(self.request, messages.SUCCESS, "Periodo Letivo Cadastrado com sucesso!")
        return reverse('school:semester_create')

class SemesterUpdate(UpdateView, ListView):
    model = Semester
    template_name = 'semester/semester_edit.html'
    form_class = SemesterForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Periodo Letivo Alterado com sucesso!")
        return reverse('school:semester_create')

class SemesterDelete(DeleteView):
    model = Semester
    template_name = 'semester/semester_confirm_delete.html'
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Periodo Letivo Removido com sucesso!")
        return reverse('school:semester_create')



############### Turmas ###############
class GradeCreate(CreateView, ListView):
    model = Grade
    template_name = 'grade/grade_add.html'
    form_class = GradeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semester_pk = self.kwargs['semester_pk']
        semester = get_object_or_404(Semester, pk=semester_pk)
        grades = Grade.objects.filter(semester = semester_pk)

        context.update({
            'semester':semester,
			'object_list': grades,
		    })

        return context

    def form_valid(self, form):
        grade = form.save(commit=False)
        semester_pk = self.kwargs['semester_pk'] 
        semester = get_object_or_404(Semester, pk=semester_pk) 

        grade.semester = semester
        grade.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Turma Cadastrada com sucesso!")
        return reverse('school:grade_create', kwargs={'semester_pk': self.kwargs['semester_pk']})
   
class GradeUpdate(UpdateView, ListView):
    model = Grade
    template_name = 'grade/grade_edit.html'
    form_class = GradeForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semester_pk = self.kwargs['semester_pk']
        semester = get_object_or_404(Semester, pk=semester_pk)
        grades = Grade.objects.filter(semester = semester_pk)

        context.update({
            'semester':semester,
			'object_list': grades,
		    })

        return context

    def form_valid(self, form):
        grade = form.save(commit=False)
        semester_pk = self.kwargs['semester_pk'] 
        semester = get_object_or_404(Semester, pk=semester_pk) 

        grade.semester = semester
        grade.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Turma Alterada com sucesso!")
        return reverse('school:grade_create', kwargs={'semester_pk': self.kwargs['semester_pk']})

class GradeDelete(DeleteView):
    model = Grade
    template_name = 'grade/grade_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        semester_pk = self.kwargs['semester_pk']
        semester = get_object_or_404(Semester, pk=semester_pk)
        context.update({
            'semester':semester,
		})

        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Turma Removida com sucesso!")
        return reverse('school:grade_create', kwargs={'semester_pk': self.kwargs['semester_pk']})


def gerarCor():
    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return color


############### Componente Curricular - Disciplina ###############
class CurricularComponentCreate(CreateView, ListView):
    model = CurricularComponent
    # template_name = 'curricular_component/curricular_component_add.html'
    # template_name = 'curricular_component/curricular_component_add_colapse.html'
    template_name = 'curricular_component/curricular_component_add_backup.html'
    form_class = CurricularComponentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grade_pk = self.kwargs['grade_pk']
        grade = get_object_or_404(Grade, pk=grade_pk)
        curricular_components = CurricularComponent.objects.filter(grade = grade_pk)

        random_color = gerarCor()
        context.update({
            'grade':grade,
			'object_list': curricular_components,
            'random_color':random_color,
		    })

        return context

    def form_valid(self, form):
        curricular_component = form.save(commit=False)
        grade_pk = self.kwargs['grade_pk'] 
        grade = get_object_or_404(Grade, pk=grade_pk) 

        curricular_component.grade = grade
        curricular_component.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Componente Curricular Cadastrado com sucesso!")
        return reverse('school:curricular_component_create', kwargs={'grade_pk': self.kwargs['grade_pk']})
   
class CurricularComponentUpdate(UpdateView, ListView):
    model = CurricularComponent
    template_name = 'curricular_component/curricular_component_edit.html'
    form_class = CurricularComponentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grade_pk = self.kwargs['grade_pk']
        grade = get_object_or_404(Grade, pk=grade_pk)
        curricular_components = CurricularComponent.objects.filter(grade = grade_pk)

        context.update({
            'grade':grade,
			'object_list': curricular_components,
		    })

        return context

    def form_valid(self, form):
        curricular_component = form.save(commit=False)
        grade_pk = self.kwargs['grade_pk'] 
        grade = get_object_or_404(Grade, pk=grade_pk) 

        curricular_component.grade = grade
        curricular_component.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Componente Curricular Alterado com sucesso!")
        return reverse('school:curricular_component_create', kwargs={'grade_pk': self.kwargs['grade_pk']})

class CurricularComponentDelete(DeleteView):
    model = CurricularComponent
    template_name = 'curricular_component/curricular_component_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        grade_pk = self.kwargs['grade_pk']
        grade = get_object_or_404(Grade, pk=grade_pk)
        context.update({
            'grade':grade,
		})

        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Componente Curricular Removido com sucesso!")
        return reverse('school:curricular_component_create', kwargs={'grade_pk': self.kwargs['grade_pk']})



############### HORÁRIOS ESCOLARES ###############
class ScheduleSemester(ListView):
    model = Semester
    template_name = 'schedule/semester.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
      
    #     context.update({
	# 		'object_list': curricular_components,
	# 	    })

    #     return context

class ScheduleSemesterGrade(ListView):
    model = Grade
    template_name = 'schedule/semester_grade.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semester_pk = self.kwargs['semester_pk']
        semester = get_object_or_404(Semester, pk=semester_pk)
        grades = Grade.objects.filter(semester = semester_pk)

        context.update({
            'semester':semester,
			'object_list': grades,
		    })

        return context

class ScheduleCurricularComponent(ListView):
    model = CurricularComponent
    template_name = 'schedule/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grade_pk = self.kwargs['grade_pk']
        grade = get_object_or_404(Grade, pk=grade_pk)
        curricular_components = CurricularComponent.objects.filter(grade = grade_pk)

        random_color = gerarCor()
        context.update({
            'grade':grade,
			'object_list': curricular_components,
            'random_color':random_color,
		    })

        return context


def ScheduleCreate(request):
    if request.method == 'POST':
        curricular_component = request.POST['curricular_component']
        curricular_component = get_object_or_404(CurricularComponent, pk=curricular_component)
        weekday = request.POST['weekday']
        dropzone = request.POST['dropzone']
        horario = Schedule(curricular_component=curricular_component,weekday=weekday,dropzone=dropzone)
        horario.save()
        return JsonResponse({'codigo':1})
    else:
	    return JsonResponse({'codigo':0})