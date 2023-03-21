from django.db import models
from django.conf import settings

from location_field.models.plain import PlainLocationField


class Place(models.Model):
    parent_place = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'])


DATABASE_ENGINE = settings.DATABASES["default"]["ENGINE"]
if DATABASE_ENGINE == 'django.contrib.gis.db.backends.spatialite':
    from location_field.models.spatial import LocationField
    class SpatialPlace(models.Model):
        parent_place = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
        city = models.CharField(max_length=255)
        location = LocationField(based_fields=['city'], zoom=7)
