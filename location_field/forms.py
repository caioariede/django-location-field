from django.forms import fields
from django.contrib.gis.geos import Point
from location_field.widgets import LocationWidget


class PlainLocationField(fields.CharField):
    def __init__(self, based_fields=None, zoom=None, default=None,
                 *args, **kwargs):
        kwargs['initial'] = default

        self.widget = LocationWidget(based_fields=based_fields, zoom=zoom,
                                     **kwargs)

        dwargs = {
            'required': True,
            'label': None,
            'initial': None,
            'help_text': None,
            'error_messages': None,
            'show_hidden_initial': False,
        }

        for attr in dwargs:
            if attr in kwargs:
                dwargs[attr] = kwargs[attr]

        super(PlainLocationField, self).__init__(*args, **dwargs)


class LocationField(PlainLocationField):
    def clean(self, value):
        lat, lng = value.split(',')
        return Point(float(lat), float(lng))
