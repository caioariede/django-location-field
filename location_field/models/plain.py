from django.db.models import CharField

from location_field.forms import plain as forms
from location_field.models.base import BaseLocationField


class PlainLocationField(BaseLocationField, CharField):
    formfield_class = forms.PlainLocationField

    def __init__(self, max_length=63, *args, **kwargs):
        super(PlainLocationField, self).__init__(*args, **kwargs)

        kwargs.pop('based_fields', None)
        kwargs.pop('zoom', None)
        kwargs.pop('suffix', None)

        CharField.__init__(self, max_length=max_length, *args, **kwargs)
