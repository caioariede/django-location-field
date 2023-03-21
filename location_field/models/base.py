from django.conf import settings


class BaseLocationField(object):
    def __init__(self, **kwargs):
        self._based_fields = kwargs.pop("based_fields", [])
        self._zoom = kwargs.pop("zoom", 13)

    def formfield(self, **kwargs):
        return super(BaseLocationField, self).formfield(
            form_class=self.formfield_class,
            based_fields=self._based_fields,
            zoom=self._zoom,
            **kwargs
        )
