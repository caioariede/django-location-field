***************
Getting started
***************

Installation
============

Using pip::

    pip install django-location-field


Configuration
=============

Add ``location_field.apps.DefaultConfig`` to ``INSTALLED_APPS``.

Example:

.. code-block:: python

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',

        'location_field.apps.DefaultConfig',
    ]


Choose a map provider
---------------------

At this moment we support three map providers:

- `Google <providers.html#google>`__
- `Mapbox <providers.html#mapbox>`__
- `OpenStreetMap <providers.html#openstreetmap>`__


Choose a search provider
------------------------

At this moment we support three search providers:

- `Google <providers.html#google>`__
- `Yandex <https://tech.yandex.com/maps/geocoder/>`__
- `Nominatim <https://wiki.openstreetmap.org/wiki/Nominatim>`__


Rendering form with a map
=========================

**NOTE:** If you will be using the map widget only inside Django admin, you can
skip this section as it should work out-of-the-box.

The way to render a form containing a map is the same as any other forms
containing their own javascript and stylesheets, except that you need to ensure
your page loads ``jQuery``.

.. code-block:: html

   <head>
      <script src="[ link to jquery.js goes here ]"></script>
      {{form.media}}
   </head>
   <body>
      {{form}}
   </body>

You can find a running example in the example app (``example/`` directory).
