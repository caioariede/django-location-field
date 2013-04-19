from django.forms import widgets
from django.utils.safestring import mark_safe


class LocationWidget(widgets.TextInput):
    show_input = False

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

        based_fields = map(lambda f: \
            '$("#id_%s")' % (prefix + f.name,), self.based_fields)

        text_input = super(LocationWidget, self).render(name, value, attrs)
        map_div = u'''
<div style="margin:4px 0 0 0">
    <div id="map_%(name)s" style="width: 500px; height: 250px"></div>
</div>
<script type="text/javascript">
    location_field_load(
        $('#map_%(name)s'), $([%(based_fields)s]), %(zoom)d, %(show_input)d)
</script>
'''
        return mark_safe(text_input + map_div % {
            'name': name,
            'based_fields': ','.join(based_fields),
            'zoom': self.zoom,
            'show_input': self.show_input,
        })

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js',
            'http://maps.google.com/maps/api/js?sensor=false',
            '/location_field/media/form.js',
        )
