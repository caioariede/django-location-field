import six
import json

from django.conf import settings
from django import forms
from django.forms import widgets
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class LocationWidget(widgets.TextInput):
    def __init__(self, **kwargs):
        attrs = kwargs.pop('attrs', None)

        self.options = dict(settings.LOCATION_FIELD)
        self.options['field_options'] = {
            'based_fields': kwargs.pop('based_fields'),
        }

        super(LocationWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        if value is not None:
            try:
                if isinstance(value, six.string_types):
                    lat, lng = value.split(',')
                else:
                    lng = value.x
                    lat = value.y

                value = '%s,%s' % (
                    float(lat),
                    float(lng),
                )
            except ValueError:
                value = ''
        else:
            value = ''

        if '-' not in name:
            prefix = ''
        else:
            prefix = name[:name.rindex('-') + 1]

        self.options['field_options']['prefix'] = prefix

        attrs = attrs or {}
        attrs['data-location-field-options'] = json.dumps(self.options)

        # Django added renderer parameter in 1.11, made it mandatory in 2.1
        try:
            text_input = super(LocationWidget, self).render(name, value, attrs=attrs, renderer=renderer)
        except TypeError:
            text_input = super(LocationWidget, self).render(name, value, attrs=attrs)

        return render_to_string('location_field/map_widget.html', {
            'field_name': name,
            'field_input': mark_safe(text_input)
        })

    @property
    def media(self):
        return forms.Media(**settings.LOCATION_FIELD['resources.media'])
