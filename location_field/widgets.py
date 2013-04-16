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
                value = value.split(',')

            value = '%s,%s' % (
                float(value[0]),
                float(value[1]),
            )
        else:
            value = ''

        based_fields = map(lambda f: '$("#id_%s")' % f.name, self.based_fields)
        text_input = super(LocationWidget, self).render(name, value, attrs)
        map_div = u'''
<div style="margin:4px 0 0 0">
    <label></label>
    <div id="map_%(name)s" style="width: 500px; height: 250px"></div>
</div>
<script type="text/javascript">
    location_field_load(
        $('#map_%(name)s'), $([%(based_fields)s]), %(zoom)d)
</script>
'''
        return mark_safe(text_input + map_div % {
            'name': name,
            'based_fields': ','.join(based_fields),
            'zoom': self.zoom,
        })

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js',
            'http://maps.google.com/maps/api/js?sensor=false',
            '/location_field/media/form.js',
        )
