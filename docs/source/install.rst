Installation
============

Using pip::

    pip install django-location-field


And add ``location_field.apps.DefaultConfig`` to ``INSTALLED_APPS``.


Default settings
----------------

These are the default settings:


.. code-block:: python

    LOCATION_FIELD_PATH = settings.STATIC_URL + 'location_field'

    LOCATION_FIELD = {
        'map.provider': 'google',
        'map.zoom': 13,

        'search.provider': 'google',
        'search.suffix': '',

        # Google
        'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
        'provider.google.api_key': '',
        'provider.google.api_libraries': '',
        'provider.google.map.type': 'ROADMAP',

        # Mapbox
        'provider.mapbox.access_token': '',
        'provider.mapbox.max_zoom': 18,
        'provider.mapbox.id': 'mapbox.streets',

        # OpenStreetMap
        'provider.openstreetmap.max_zoom': 18,

        # misc
        'resources.root_path': LOCATION_FIELD_PATH,
        'resources.media': {
            'js': (
                LOCATION_FIELD_PATH + '/js/jquery.livequery.js',
                LOCATION_FIELD_PATH + '/js/form.js',
            ),
        },
    }


Override default settings
-------------------------

To override the default settings, you can define only what you want to
override, for example:

.. code-block:: python

    LOCATION_FIELD = {
        'map.provider': 'openstreetmap',
    }

This will keep all other settings the same.
