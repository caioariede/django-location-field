from django.forms import widgets

class LocationWidget(widgets.MultiWidget):
    def __init__(self, attrs=None, **kwargs):
        based_fields = []
        zoom = 13
        if 'based_fields' in kwargs:
            based_fields = [f.name for f in kwargs['based_fields']]
        if 'zoom' in kwargs:
            zoom = kwargs['zoom']
        txt_widget = widgets.TextInput(attrs=dict(attrs or {}, **{'size': 30}))
        map_widget = GMapWidget(based_fields, zoom, attrs=attrs)
        super(LocationWidget, self).__init__((txt_widget, map_widget), attrs)

    def decompress(self, value):
        return [value, value]

    def format_output(self, widgets_list):
        return widgets_list[0] + '<div style="margin:4px 0 0 0"><label></label>' + widgets_list[1] + '</div>'

class GMapWidget(widgets.HiddenInput):
    def __init__(self, based_fields, zoom, attrs=None):
        self.based_fields = based_fields
        self.zoom = zoom
        super(GMapWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        based_fields = map(lambda f: '$("#id_%s")' % f, self.based_fields);
        return super(GMapWidget, self).render(name, value, attrs)\
             + ('<div id="map_%(name)s" style="width: 500px; height: 250px"></div>'\
             + '<script type="text/javascript">location_field_load($(\'#map_%(name)s\'), $([%(based_fields)s]), %(zoom)d)</script>')\
             % {'name': name, 'based_fields': ','.join(based_fields), 'zoom': self.zoom}

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js',
            'http://maps.google.com/maps/api/js?sensor=false',
            '/location_field/media/form.js',
        )
