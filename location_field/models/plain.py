from django.db.models import CharField

from location_field.forms import plain as forms
from location_field.models.base import BaseLocationField


class PlainLocationField(BaseLocationField, CharField):
    formfield_class = forms.PlainLocationField

    def __init__(self, based_fields=None, zoom=None, suffix='',
                 max_length=63, *args, **kwargs):

        super(PlainLocationField, self).__init__(based_fields=based_fields,
                                                 zoom=zoom, suffix=suffix, *args, **kwargs)

        CharField.__init__(self, max_length=max_length, *args, **kwargs)


# south compatibility
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^location_field\.models\.plain\.PlainLocationField"])
except:
    pass
