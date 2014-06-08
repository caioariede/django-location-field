from django.contrib.gis.geos import Point

from location_field.forms.plain import PlainLocationField


class LocationField(PlainLocationField):
    def clean(self, value):
        if not value:
            return None

        lat, lng = value.split(',')
        return Point(float(lng), float(lat))

