from django.apps import AppConfig
from django.conf import settings

from location_field.settings import LOCATION_FIELD


class DefaultConfig(AppConfig):
    name = 'location_field'
    verbose_name = 'Location Field'

    def ready(self):
        self.patch_settings()

    def patch_settings(self):
        if not hasattr(settings, 'LOCATION_FIELD'):
            settings.LOCATION_FIELD = LOCATION_FIELD
        else:
            settings.LOCATION_FIELD.update(LOCATION_FIELD)
