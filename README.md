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

**MIT License**

<pre>Copyright (c) 2011 Caio Ariede and Codasus Technologies.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.</pre>
