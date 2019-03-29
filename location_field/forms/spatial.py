from django.contrib.gis.geos import Point

from location_field.forms.plain import PlainLocationField


class LocationField(PlainLocationField):
    def clean(self, value):
        try:
            lat, lng = value.split(',')
            return Point(float(lng), float(lat))
        except ValueError:
            return None

    def _coerce(self, value):
        """
        Coerce coordinates for checking changed values.

        Sometimes we have a Point, and sometimes we have a string.
        In this case, turning the Points into strings is fine, because
        we're only bound to have one SRID.
        """
        if isinstance(value, Point):
            return '{y},{x}'.format(x=value.x, y=value.y)
        return value
    
