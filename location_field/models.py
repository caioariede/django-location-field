from django.db import models

from forms import LocationField as LocationFormField

class LocationField(models.Field):
    def __init__(self, *args, **kwargs):
        self.based_fields = kwargs.pop('based_fields') if 'based_fields' in kwargs else []
        self.zoom = kwargs.pop('zoom') if 'zoom' in kwargs else 13
        super(LocationField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        dwargs = {'form_class': LocationFormField, 'based_fields': self.based_fields, 'zoom': self.zoom, 'model_field': self}
        dwargs.update(kwargs)
        return super(LocationField, self).formfield(**dwargs)

# south compatibility
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^location_field\.models\.LocationField"])
except:
    pass
