from django.apps import AppConfig
from django.conf import settings

from location_field.settings import LOCATION_FIELD


class DefaultConfig(AppConfig):
    name = "location_field"
    verbose_name = "Location Field"

    def ready(self):
        self.patch_settings()

    def patch_settings(self):
        config = LOCATION_FIELD.copy()
        config.update(getattr(settings, "LOCATION_FIELD", {}))

        settings.LOCATION_FIELD = config
