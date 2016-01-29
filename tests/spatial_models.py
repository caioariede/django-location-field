from django.db import models

from location_field.models.spatial import LocationField


class SpatialPlace(models.Model):
    parent_place = models.ForeignKey('self', blank=True, null=True)
    city = models.CharField(max_length=255)
    location = LocationField(based_fields=['city'], zoom=7)
