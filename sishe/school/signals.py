from django.db.models.signals import post_save, pre_save, post_delete, m2m_changed
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from sishe.school.models import CurricularComponent, Schedule


################### LEMBRETE SOBRE SIGNALS ################### 
# é necessario criar o sinal em signals.py, 
# Em seguida adicionar, no arquivo __init__.py: default_app_config = 'nomeDoProjeto.nomeDoApp.apps.nomeDoAppConfig'
# por fim, adiciona no arquivo apps.py:
# def ready(self):
#     import nomeDoProjeto.nomeDoApp.signals
#############################################################


# Essa função é um sinal acionado após salvar um componente curricular,
# São criados x horarios da disciplina de acordo com a carga horaria semanal,
# Esses horários serão os cards que usarei para o drag and drop nas dropzones de horarios
@receiver(post_save, sender=CurricularComponent)
def create_schedule_dropzone(sender, instance, created, **kwargs):
    schedules = Schedule.objects.filter(curricular_component=instance)
    number_schedules = schedules.count()

    if number_schedules == 0:
        # create (primeiro cadastro)
        print("primeiro cadastro -------------------------")
        for i in range(instance.weekly_workload):
            Schedule.objects.create(curricular_component=instance)
    else:
        # update
        # diminuiu a carga horaria semanal
        if number_schedules > instance.weekly_workload:
            for i in range(abs(number_schedules-instance.weekly_workload)):
                schedules[i].delete() 
        # aumentou a carga horaria semanal
        elif number_schedules < instance.weekly_workload:
            for i in range(abs(number_schedules-instance.weekly_workload)):
                Schedule.objects.create(curricular_component=instance)
        pass
    pass




# @receiver(post_save, sender=CurricularComponent)
# def create_schedule_dropzone(sender, instance, created, **kwargs):
#     if not Schedule.objects.filter(curricular_component=instance).exists():
#         for i in range(instance.weekly_workload):
#             Schedule.objects.create(curricular_component=instance)
# --------------------------------------------------------

# @receiver(post_save, sender=CurricularComponent)
# def create_schedule(sender, instance, created, **kwargs):
#     print("------------------- aqui estou")
#     if created:
#         print("------------------- aqui estou novamente")
#         Schedule.objects.create(curricular_component=instance)
  
