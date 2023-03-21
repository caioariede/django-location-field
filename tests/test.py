import json

import pytest
from django.test import TestCase
from pyquery import PyQuery as pq

import location_field
from location_field.apps import DefaultConfig
from tests.forms import LocationForm
from tests.models import Place


@pytest.mark.django_db
def test_plain():
    vals = {
        "city": "Bauru",
        "location": "-22.2878573,-49.0905487",
    }

    obj = Place.objects.create(**vals)

    assert obj.city == "Bauru"
    assert obj.location == "-22.2878573,-49.0905487"


def test_settings(settings):
    settings.LOCATION_FIELD = {"map.provider": "foobar"}
    app_config = DefaultConfig("location_field", location_field)
    app_config.patch_settings()

    assert settings.LOCATION_FIELD.get("map.provider") == "foobar"


@pytest.mark.django_db
def test_field_options(settings):
    form = LocationForm(initial={})
    d = pq(str(form))

    opts = json.loads(
        d("[data-location-field-options]").attr("data-location-field-options")
    )

    location_field_opts = settings.LOCATION_FIELD

    for key, value in location_field_opts.items():
        assert value == opts[key]


def test_custom_resources(settings):
    form = LocationForm(initial={})

    assert "form.js" in str(form.media)

    settings.LOCATION_FIELD = {"resources.media": {"js": ["foo.js", "bar.js"]}}
    assert "foo.js" in str(form.media)
    assert "bar.js" in str(form.media)
