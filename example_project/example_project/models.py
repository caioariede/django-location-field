from django.db import models
from django.contrib.gis.geos import Point

from location_field.models import LocationField, PlainLocationField


class Chain(models.Model):
    name = models.CharField(max_length=255)


class Place(models.Model):
    chain = models.ForeignKey(Chain, related_name='places')

    city = models.CharField(max_length=255)

    plain_location = PlainLocationField(based_fields=[city], zoom=7,
                                        default=Point(1, 1))

    geo_location = LocationField(based_fields=[city], zoom=7,
                                 default=Point(1, 1))

    def __str__(self):
        return self.city

    def get_distance_from(self, another_place):
        return self.geo_location.distance(another_place.geo_location)
