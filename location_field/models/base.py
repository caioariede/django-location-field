class BaseLocationField(object):
    def __init__(self, based_fields=[], zoom=2, default=None, suffix='', *args, **kwargs):
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
