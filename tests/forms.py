from django import forms

from tests.models import Place


class LocationForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ()
