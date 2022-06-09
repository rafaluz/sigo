from django.apps import AppConfig
# from django.utils.translation import ugettext_lazy as _

class SchoolConfig(AppConfig):
    name = 'sishe.school'
    # verbose_name = _('school')

    def ready(self):
        import sishe.school.signals

