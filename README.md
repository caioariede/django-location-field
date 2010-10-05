** Installation **

1. Put `location_field` directory in your application root.

2. Install GEOS.

    MacOSX (with brew)

    `sudo brew install geos` 

3. Open `settings.py` and set the correct engine, according to your database:

    `'ENGINE': 'django.contrib.gis.db.backends.mysql'`

** Using **

    from django.contrib.gis.db import models
    from location_field.models import LocationField

    class Place:
        city = models.CharField(max_length=255)
        location = LocationField(based_fields=[city], zoom=7)
        objects = models.GeoManager()

Look that you must put `models.GeoManager()` in your model, or some errors will occur.

And syncronize the database:

    `./manage.py syncdb`
