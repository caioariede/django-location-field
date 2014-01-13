from django.contrib.gis.db.models import PointField
from django.db.models import CharField

from location_field import forms


class BaseLocationField(object):
    def __init__(self, based_fields=None, zoom=2, default=None, suffix='', *args, **kwargs):
        if based_fields is None:
            based_fields = []
        self._based_fields = based_fields
        self._zoom = zoom
        self._default = default
        self.default = default

    def formfield(self, **kwargs):
        return super(BaseLocationField, self).formfield(
            form_class=self.formfield_class,
            based_fields=self._based_fields,
            zoom=self._zoom,
            default=self._default,
            **kwargs)


class LocationField(BaseLocationField, PointField):
    formfield_class = forms.LocationField

    def __init__(self, based_fields=None, zoom=None, suffix='', *args, **kwargs):
        super(LocationField, self).__init__(based_fields=based_fields,
                                            zoom=zoom, suffix=suffix, *args, **kwargs)

        PointField.__init__(self, *args, **kwargs)


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
    add_introspection_rules([], ["^location_field\.models\.LocationField"])
    add_introspection_rules([], ["^location_field\.models\.PlainLocationField"])
    add_introspection_rules([], ["^django\.contrib\.gis"])
except ImportError:
    pass
