from importlib import import_module
from django.apps import AppConfig


class RegistrationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.registrations"

    def import_models(self):
        self.models = self.apps.all_models[self.label]
        self.models_module = import_module(
            f"{self.name}.registration_models"
        )

    def ready(self):
        import_module(f"{self.name}.registration_admin")