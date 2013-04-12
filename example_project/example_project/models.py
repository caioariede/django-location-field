from django.db import models
from django.contrib.gis.geos import Point

from location_field.models import LocationField


class Place(models.Model):
    city = models.CharField(max_length=255)
    location = LocationField(based_fields=[city], zoom=7, default=Point(1, 1))
