Django Location Field
==

Let users pick locations using a map widget and store its latitude and longitude.

**Stable version:** [django-location-field==2.1.0](https://pypi.python.org/pypi/django-location-field/2.1.0)

**License:** MIT

Status
--

[![Build Status](https://travis-ci.org/caioariede/django-location-field.svg?branch=master)](https://travis-ci.org/caioariede/django-location-field) [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/caioariede)

Tests are performed with Python 2.7, Django 1.8 .. 1.10 and SpatiaLite. We'd like to have automated tests for Python 3 too, but it looks like pysqlite (which is used for testing) does not support it yet, so it's blocking us. You can get more details in the [tox.ini](https://github.com/caioariede/django-location-field/blob/master/tox.ini#L40) file.

Features
--

* Support for multiple map engines, like Google Maps, OpenStreetMap and Mapbox.
* Support for multiple search engines, like Google, Nominatim and Yandex.
* Works with both Spatial and non-Spatial databases.

Compatibility
--

* Django 1.8 to 1.10
* Python 2.7 to 3.5

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
