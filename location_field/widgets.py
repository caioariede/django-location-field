from django.forms import widgets
from django.utils.safestring import mark_safe


class LocationWidget(widgets.TextInput):
    def __init__(self, attrs=None, based_fields=None, zoom=None, **kwargs):
        self.based_fields = based_fields
        self.zoom = zoom
        super(LocationWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is not None:
            if type(value) == str:
                lat, lng = value.split(',')
            else:
                lng = value.x
                lat = value.y

            value = '%s,%s' % (
                float(lat),
                float(lng),
            )
        else:
            value = ''

        if '-' not in name:
            prefix = ''
        else:
            prefix = name[:name.rindex('-') + 1]

        based_fields = ','.join(
            map(lambda f: '#id_' + prefix + f.name, self.based_fields))

        attrs = attrs or {}
        attrs['data-location-widget'] = name
        attrs['data-based-fields'] = based_fields
        attrs['data-zoom'] = self.zoom
        attrs['data-map'] = '#map_' + name

        text_input = super(LocationWidget, self).render(name, value, attrs)

        map_div = u'''
<div style="margin:4px 0 0 0">
    <label></label>
    <div id="map_%(name)s" style="width: 500px; height: 250px"></div>
</div>
'''
        return mark_safe(text_input + map_div % {'name': name})

    class Media:
        js = (
            'http://maps.google.com/maps/api/js?sensor=false',
            '/location_field/media/form.js',
        )
