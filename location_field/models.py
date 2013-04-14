from django.contrib.gis.db.models import PointField

from location_field import forms


class LocationField(PointField):
    def __init__(self, based_fields=[], zoom=2, default=None, *args, **kwargs):
        self._based_fields = based_fields
        self._zoom = zoom
        self._default = default
        self.default = default
        super(LocationField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        return super(LocationField, self).formfield(
            form_class=forms.LocationField,
            based_fields=self._based_fields,
            zoom=self._zoom,
            default=self._default,
            **kwargs)

# south compatibility
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^location_field\.models\.LocationField"])
    add_introspection_rules([], ["^django\.contrib\.gis"])
except:
    pass
