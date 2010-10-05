** Installation **

1. Put _location_field_ directory in your application root.

2. Install GEOS.

    MacOSX (with brew)

    `sudo brew install geos` 

3. Set the correct engine on your `settings.py`, for example:

    `'ENGINE': 'django.contrib.gis.db.backends.mysql'`

** Using **

    from django.contrib.gis.db import models
    from location_field.models import LocationField

    class Place:
        city = models.CharField(max_length=255)
        location = LocationField(based_fields=[city], zoom=7)
        objects = models.GeoManager()

And syncronize the database:

    `./manage.py syncdb`

Look that you must put `models.GeoManager()` in your model, or some errors will occur.
