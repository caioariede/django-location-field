Getting started
===============

Installation
------------

Using pip::

    pip install django-location-field


Configuration
-------------

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

At this moment there's only one search provider:

- Google
