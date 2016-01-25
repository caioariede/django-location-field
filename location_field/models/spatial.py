from django.contrib.gis.db.models import PointField

from location_field.forms import spatial as forms
from location_field.models.base import BaseLocationField


class LocationField(BaseLocationField, PointField):
    formfield_class = forms.LocationField

    def __init__(self, *args, **kwargs):
        super(LocationField, self).__init__(*args, **kwargs)

        kwargs.pop('based_fields', None)
        kwargs.pop('zoom', None)
        kwargs.pop('suffix', None)

        PointField.__init__(self, *args, **kwargs)
