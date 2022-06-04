from logging import PlaceHolder
# from turtle import color
from django import forms
from .models import *
from dal import autocomplete
from sishe.accounts.models import User, Axis, Teacher 
import random

class TimeTableCreateForm(forms.ModelForm):
    start = forms.TimeField(
        label='Hora de Início da Aula',
        widget=forms.TextInput(
            attrs={
                'type': 'Time',
                'class': 'time',
                'format': 'HH:00',
                # 'min':'07:00',
                # 'max':'22:00',
            }
        )
    )

    class Meta:
        model = TimeTable
        fields = ('start',)

        
        
class CourseForm(forms.ModelForm):

    coordinator = forms.ModelChoiceField(
        label='Coordenador',
        queryset = User.objects.all(),
        widget = autocomplete.ModelSelect2(url='accounts:user_autocomplete'),
        # required=True,
    )

    class Meta:
        model = Course
        fields = ('name','coordinator')
        # widgets = {
        #     'coordinator': autocomplete.ModelSelect2(url='accounts:user_autocomplete'),
        # }




class SemesterForm(forms.ModelForm):
    start_date = forms.DateField(
        label='Data do Inicio',
        widget=forms.TextInput(
            attrs={
                'type': 'Date',
                'class': 'date',
            }
        )
    )

    end_date = forms.DateField(
        label='Data do Fim',
        widget=forms.TextInput(
            attrs={
                'type': 'Date',
                'class': 'date',
            }
        )
    )

    class Meta:
        model = Semester
        fields = '__all__'




class GradeForm(forms.ModelForm):

    course = forms.ModelChoiceField(
        label='Curso',
        queryset = Course.objects.all(),
        widget = autocomplete.ModelSelect2(url='school:course_autocomplete'),
    )

    class Meta:
        model = Grade
        exclude = ['semester',]
        # fields = ('__all__')



class CurricularComponentForm(forms.ModelForm):

    color = forms.CharField(
        label='Cor',
        widget=forms.TextInput(
            attrs={
                'type': 'Color',
                # 'class': 'color',
            }
        )
    )

    teacher = forms.ModelChoiceField(
        label="Professor",
        queryset= Teacher.objects.all(),
        widget= autocomplete.ModelSelect2(url='accounts:teacher_autocomplete',attrs={'placeholder':'Informe o professor ou o Eixo'})
    )

    class Meta:
        model = CurricularComponent
        exclude = ['grade',]
