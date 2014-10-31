from django.contrib.gis.geos import Point

from location_field.forms.plain import PlainLocationField


class LocationField(PlainLocationField):
    def clean(self, value):
        try:
            lat, lng = value.split(',')
            return Point(float(lng), float(lat))
        except ValueError:
            return None

