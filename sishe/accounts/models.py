from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import uuid

# Create your models here.

class AuditModel(models.Model):
    # Audit Fields
    create_on = models.DateTimeField('Criado em', auto_now_add=True)
    updated_on = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract=True


class User(AbstractUser,AuditModel):
    username = models.CharField('Email', max_length=150, default=uuid.uuid4, unique=True)
    name = models.CharField("Nome", max_length=255)
    email = models.EmailField("Email", unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)

    REQUIRED_FIELDS = ['email', 'name']

    def save(self, *args, **kwargs):
        self.username = self.email

        super(User, self).save(*args, **kwargs)


    def __str__(self):
        return self.email
    
    def first_name(self):
        return self.name.split()[0]


class Axis(AuditModel):
    name = models.CharField("Nome", max_length=255)

    def __str__(self):
        return self.name

class Teacher(AuditModel):
    name = models.CharField("Nome", max_length=255)
    GENDER_CHOICES = (('Professor', 'Professor'), ('Professora', 'Professora'))
    gender = models.CharField(u'Gênero', max_length=10, choices=GENDER_CHOICES, blank=True, help_text='*')
    SCHOOL_DAYS_CHOICES = (('Seg', 'Seg'), ('Ter', 'Ter'), ('Qua', 'Qua'), ('Qui', 'Qui'), ('Sex', 'Sex'), ('Sab', 'Sab'))
    school_days = models.CharField(u'Dias de Ensino', max_length=10, choices=SCHOOL_DAYS_CHOICES, blank=True, help_text='*')
    note = models.TextField('Observação', blank=True)
    axis = models.ForeignKey(Axis, verbose_name='Eixo', related_name='teachers', on_delete=models.CASCADE) # blank=True, null=True
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['create_on']