from django.apps import AppConfig


class HealthCheckConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'health_check'

    def ready(self):
        from .views import start_health_check_scheduler
        # To make sure the scheduler starts
        start_health_check_scheduler()
