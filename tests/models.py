from django.db import models

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
