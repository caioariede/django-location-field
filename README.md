**Installation**

1. Install through pip (or manually place it on your `PYTHON_PATH`).

    `pip install git+http://github.com/codasus/django-location-field#egg=location_field`

2. Install GEOS.

    MacOSX (with brew)

    `sudo brew install geos` 

3. Open `settings.py` and set the correct engine, according to your database:

    `'ENGINE': 'django.contrib.gis.db.backends.mysql'`

4. Open your root `urls.py` and put the line below:

    `(r'^location_field/', include('location_field.urls')),`

**Usage**

    from django.contrib.gis.db import models
    from location_field.models import LocationField

    class Place(models.Model):
        city = models.CharField(max_length=255)
        location = LocationField(based_fields=[city], zoom=7, default=Point(1, 1))
        objects = models.GeoManager()

Look that you must put `models.GeoManager()` in your model, or some errors will occur.

And syncronize the database:

`./manage.py syncdb`

**Screenshot**

![Screenshot](http://img153.imageshack.us/img153/1914/screenshot20101005at161.png)

**License**

Django Input Mask by [Codasus Technologies](http://codasus.com) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

You are free:

* to Share - to copy, distribute and transmit the work
* to Remix - to adapt the work
* to make commercial use of the work
