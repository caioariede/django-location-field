**Django Location Field**

Allows users to input locations based on latitude and longitude, using a Google maps widget.

MIT licensed

**Status**

[![Build Status](https://travis-ci.org/caioariede/django-location-field.svg?branch=master)](https://travis-ci.org/caioariede/django-location-field)

Tests are performed with Python 2.7, Django 1.7 1.8 and SpatiaLite. We'd like to have automated tests for Python 3 too, but it looks like pysqlite (which is used for testing) does not support it yet, so it's blocking us. You can get more details in the [tox.ini](https://github.com/caioariede/django-location-field/blob/master/tox.ini#L40) file.

**Features**

* The map will automatically update after changing a field based on
* Works with both Spatial and non-Spatial databases
* Works perfectly with formsets

**Compatibility**

* Django 1.7 and 1.8
* Python 2.7 and 3.x

It was only tested with PostGIS but may work with other Spatial Databases.

**Installation**

1. Install through pip (or manually place it on your `PYTHONPATH`).

    `pip install django-location-field`

2. Create a Spatial Database
3. Add `location_field` to INSTALLED_APPS your settings.py file

For example, PostGIS:

    https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis/

**Basic usage (using Spatial Database)**

    from django.contrib.gis.db import models
    from django.contrib.gis.geos import Point
    from location_field.models.spatial import LocationField

    class Place(models.Model):
        city = models.CharField(max_length=255)
        location = LocationField(based_fields=[city], zoom=7, default='Point(1.0 1.0)')
        objects = models.GeoManager()

Look that you must put `models.GeoManager()` in your model, or some errors will occur.

**Basic usage (without Spatial Database)**

    from django.db import models
    from location_field.models.plain import PlainLocationField

    class Place(models.Model):
        city = models.CharField(max_length=255)
        location = PlainLocationField(based_fields=[city], zoom=7)

**Screenshot**

![Screenshot](https://github.com/caioariede/django-location-field/raw/master/screenshot.png)
