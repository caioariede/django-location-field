![logo](django-location-field.png)

django-location-field
==

Let users pick locations using a map widget and store its latitude and longitude.

**Documentation:** [https://django-location-field.readthedocs.io/en/latest/](https://django-location-field.readthedocs.io/en/latest/)  
**License:** MIT

Status
--

[![PyPI!](https://img.shields.io/pypi/v/django-location-field)](https://pypi.org/project/django-location-field/)
[![PyPI - Downloads!](https://img.shields.io/pypi/dm/django-location-field?color=blue)](https://pypi.org/project/django-location-field/)
[![Build](https://github.com/caioariede/django-location-field/actions/workflows/ci.yaml/badge.svg)](https://github.com/caioariede/django-location-field/actions/workflows/ci.yaml)
[![Documentation Status](https://readthedocs.org/projects/django-location-field/badge/?version=latest)](https://django-location-field.readthedocs.io/en/latest/?badge=latest)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-blue.svg)](https://saythanks.io/to/caioariede)


Tests are performed with Python 2 and 3, Django 1.11 and 2, and SpatiaLite.

Features
--

* Support for multiple map engines, like Google Maps, OpenStreetMap and Mapbox.
* Support for multiple search engines, like Google, Nominatim, Yandex and Addok.
* Works with both Spatial and non-Spatial databases.

Compatibility
--

* Django: 1.11, 2.2, 3.2
* Python 2.7, 3.9, 3.10, 3.11

Spatial Databases
--

* PostGIS
* SpatiaLite

Installation
--

1. Install through pip (or manually place it on your `PYTHONPATH`).

    `pip install django-location-field`

2. Add `location_field.apps.DefaultConfig` to `INSTALLED_APPS` your **settings.py** file

For example, PostGIS:

    https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis/

Basic usage (using Spatial Database)
--

```python
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

class Place(models.Model):
    city = models.CharField(max_length=255)
    location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
```

Basic usage (without Spatial Database)
--

```python
from django.db import models
from location_field.models.plain import PlainLocationField

class Place(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
```

Screenshot
--

![Screenshot](https://github.com/caioariede/django-location-field/raw/master/screenshot.png)

---

[Nick Frost](https://www.iconfinder.com/Gimpopo) has credit over the [image](django-location-field.png) used as logo for this project. [CC BY](https://creativecommons.org/licenses/by/3.0/)
