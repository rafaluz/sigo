from django import forms
from .models import *

# class TimeTableCreateForm(forms.ModelForm):

#     class Meta():
#         model = TimeTable
#         fields = ['start']

#         widgets = {
#             'start': forms.TimeInput(format='%H:%M'),
#             # 'start': forms.TimeInput(attrs={'type': 'time'})
#         }


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

        
        
	