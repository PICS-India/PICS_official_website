from importlib import import_module
from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.events"

    def import_models(self):
        self.models = self.apps.all_models[self.label]
        self.models_module = import_module(
            f"{self.name}.event_models"
        )

    def ready(self):
        import_module(f"{self.name}.event_admin")