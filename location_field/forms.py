from django.forms import fields
from django.contrib.gis.geos import Point
from location_field.widgets import LocationWidget

class LocationField(fields.CharField):
    def __init__(self, *args, **kwargs):
        self.widget = LocationWidget(**kwargs)
        super(LocationField, self).__init__(*args)

    def clean(self, value):
        lat, lng = value.split(',')
        return Point(int(float(lat) * 1000000), int(float(lng) * 1000000))
