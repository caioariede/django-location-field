**Django Location Field**

Allows users to input locations based on latitude and longitude, using a
Google maps widget.

*Currently it does not work with non-Spatial Databases.*

MIT licensed

**Compatibility**

* Django 1.3, 1.4 and 1.5
* Python 2.6, 2.7

It was only tested with PostGIS 1.5+ but may work with other Spatial Databases.

**Installation**

1. Install through pip (or manually place it on your `PYTHON_PATH`).

    `pip install git+http://github.com/codasus/django-location-field#egg=location_field`

2. Create a Spatial Database

For example, PostGIS:

    https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis/

**Configuration**

See the [example project](example_project/).

**Basic usage**

    from django.contrib.gis.db import models
    from location_field.models import LocationField

    class Place(models.Model):
        city = models.CharField(max_length=255)
        location = LocationField(based_fields=[city], zoom=7, default=Point(1, 1))
        objects = models.GeoManager()

Look that you must put `models.GeoManager()` in your model, or some errors will occur.

**Screenshot**

![Screenshot](http://img153.imageshack.us/img153/1914/screenshot20101005at161.png)
