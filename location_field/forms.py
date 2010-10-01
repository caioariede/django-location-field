from django.forms import fields
from location_field.widgets import LocationWidget

class LocationField(fields.MultiValueField):
    def __init__(self, *args, **kwargs):
        self.widget = LocationWidget(**kwargs)

        fields_list = (
            fields.CharField(),
            fields.CharField(),
        )

        super(LocationField, self).__init__(fields_list, *args)

    def compress(self, data_list):
        return data_list[0]
