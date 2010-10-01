from django.db import models

from forms import LocationField as LocationFormField

class LocationField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.zoom = 13
        self.based_fields = []
        if 'based_fields' in kwargs:
            self.based_fields = kwargs['based_fields']
            del kwargs['based_fields']
        if 'zoom' in kwargs:
            self.zoom = kwargs['zoom']
            del kwargs['zoom']
        kwargs = dict({'max_length': 54, 'blank': True}, **kwargs)
        super(LocationField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': LocationFormField, 'based_fields': self.based_fields, 'zoom': self.zoom, 'model_field': self}
        defaults.update(kwargs)
        return super(LocationField, self).formfield(**defaults)

# south compatibility
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^location_field\.models\.LocationField"])
except:
    pass
