from django.contrib.gis.db.models import PointField

from location_field.forms import spatial as forms
from location_field.models.base import BaseLocationField


class LocationField(BaseLocationField, PointField):
    formfield_class = forms.LocationField

    def __init__(self, based_fields=None, zoom=None, suffix='', *args, **kwargs):
        super(LocationField, self).__init__(based_fields=based_fields,
                                            zoom=zoom, suffix=suffix, *args, **kwargs)

        PointField.__init__(self, *args, **kwargs)


# south compatibility
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^location_field\.models\.spatial.\LocationField"])
    add_introspection_rules([], ["^django\.contrib\.gis"])
except:
    pass
