from pyexpat import model
from django.db import models
from sishe.accounts.models import AuditModel, Teacher, User
# from colorfield.fields import ColorField

# Curso
class Course(AuditModel):
    name = models.CharField('Nome', max_length=255)
    coordinator = models.ForeignKey(User, verbose_name='User', related_name='courses', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['create_on']

# Periodo Letivo
class Semester(AuditModel):
    name = models.CharField('Nome',max_length=255)
    start_date = models.DateField('Data de Inicio')
    end_date = models.DateField('Data de Fim')
    
    def __str__(self):
        return self.name

# # Turno
# class ClassShift(AuditModel):
#     name = models.CharField('Nome',max_length=255)
    
#     def __str__(self):
#         return self.name

# # Horário das aulas
# class TimeTable(AuditModel):
#     start = models.TimeField('Hora de Início da Aula')
#     class_shift = models.ForeignKey(ClassShift, verbose_name='ClassShift', related_name='timetables', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return str(self.start)

#     class Meta:
#         verbose_name = 'TimeTable'
#         verbose_name_plural = 'TimeTables'
#         ordering = ['create_on']


# Turma
class Grade(AuditModel):
    course = models.ForeignKey(Course, verbose_name='Course', related_name='grades', on_delete=models.CASCADE)
    MODE_CHOICES = (('Integrado', 'Integrado'), ('Subsequente', 'Subsequente'), ('Superior', 'Superior'))
    mode = models.CharField(u'Forma', max_length=11, choices=MODE_CHOICES, blank=True, help_text='*',default='Integrado')
    period = models.IntegerField("Periodo Letivo")
    # class_shift = models.ForeignKey(ClassShift, verbose_name='ClassShift', related_name='grades', on_delete=models.CASCADE)
    CLASS_SHIFT_CHOICES = (('0', 'Diurno/Manhã'), ('1', 'Diurno/Tarde'), ('2', 'Diurno/Integral'), ('3', 'Noturno'))
    class_shift = models.CharField(u'Turno', max_length=15, choices=CLASS_SHIFT_CHOICES, blank=True, help_text='*',default='0')
    semester = models.ForeignKey(Semester, verbose_name='Semester', related_name='grades', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.period) + "º Módulo/Periodo - " + str(self.mode) 

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['create_on']

# Componente curricular (Disciplina)
    
class CurricularComponent(AuditModel):
    name = models.CharField('Nome',max_length=255)
    grade = models.ForeignKey(Grade, verbose_name='Grade', related_name='curricular_components', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='Teacher', related_name='curricular_components', on_delete=models.CASCADE)
    total_workload = models.IntegerField("Carga horária total")
    weekly_workload = models.IntegerField("Carga horária semanal") # integer or choice?
    color = models.CharField('Cor',max_length=255, default='#FF0000')
    # color = ColorField(default='#FF0000')
    
    CORE_CHOICES = (('Basico', 'Basico'), ('Tecnologico', 'Tecnologico'), ('Integrador', 'Integrador'), ('Complementar', 'Complementar'))
    core = models.CharField(u'Núcleo', max_length=12, choices=CORE_CHOICES, blank=True, help_text='*')
    
    TYPE_CHOICES = (('Regular', 'Regular'), ('Progressao Parcial', 'Progressao Parcial'))
    type = models.CharField(u'Tipo', max_length=18, choices=TYPE_CHOICES, blank=True, help_text='*', default='Regular')
    
    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'CurricularComponent'
        verbose_name_plural = 'CurricularComponents'
        ordering = ['create_on']

# Horário
class Schedule(AuditModel):
    # semester = models.ForeignKey(Semester, verbose_name='Semester', related_name='schedules', on_delete=models.CASCADE)
    # grade = models.ForeignKey(Grade, verbose_name='Grade', related_name='schedules', on_delete=models.CASCADE)
    curricular_component = models.ForeignKey(CurricularComponent, verbose_name='CurricularComponent', related_name='schedules', on_delete=models.CASCADE)
    WEEKDAY_DAYS_CHOICES = (('Seg', 'Seg'), ('Ter', 'Ter'), ('Qua', 'Qua'), ('Qui', 'Qui'), ('Sex', 'Sex'), ('Sab', 'Sab'))
    weekday = models.CharField(u'Dia da semana', max_length=3, choices=WEEKDAY_DAYS_CHOICES, blank=True, help_text='*')
    # time_table = models.ForeignKey(TimeTable, verbose_name='TimeTable', related_name='schedules', on_delete=models.CASCADE)
    start = models.TimeField('Hora de Início da Aula', blank=True, null=True)
    # dropzone = models.CharField('Dropzone', max_length=12, null=True, blank=True)
    
    def __str__(self):
        return str(self.curricular_component) + " - " + str(self.curricular_component.teacher) + " - " + str(self.weekday) + " - " + str(self.start) 

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
        ordering = ['create_on']

    def showTeacher(self):
        return self.curricular_component.teacher
    
    def showGrade(self):
        return self.curricular_component.grade
    
    def showCourse(self):
        return self.curricular_component.grade.course

    def to_dict(self):
        # from datetime import datetime, time, timedelta, timezone
        # import time
        # start = str(self.start)
        # print("--------------", start[:5])
        # start = time.strptime(self.start, "%H:%M")
        # print("---------------------------", start)
        return {
            'id':self.id,
            'curricular_component':self.curricular_component.name,
            'weekday':self.weekday,
            'start': str(self.start)[:5],
            'teacher':self.curricular_component.teacher.name,
            'school_days':self.curricular_component.teacher.school_days,
            'grade_period':self.curricular_component.grade.period,
            'grade_mode':self.curricular_component.grade.mode,
            'course':self.curricular_component.grade.course.name,
        }
    
    # def to_dict(self):
    #     data = [self.id, self.curricular_component, self.weekday, self.start, self.curricular_component.teacher, self.curricular_component.grade, self.curricular_component.grade.course]
    #     return data