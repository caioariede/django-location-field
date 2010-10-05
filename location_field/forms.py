from django.forms import fields
from location_field.widgets import LocationWidget

class LocationField(fields.CharField):
    def __init__(self, *args, **kwargs):
        self.widget = LocationWidget(**kwargs)
        super(LocationField, self).__init__(*args)
