********
Settings
********

.. _settings:

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
        'provider.google.api_key': '',
        'provider.google.map.type': 'ROADMAP',

        # Mapbox
        'provider.mapbox.access_token': '',
        'provider.mapbox.max_zoom': 18,
        'provider.mapbox.id': 'mapbox.streets',

        # OpenStreetMap
        'provider.openstreetmap.max_zoom': 18,

        # Yandex (Only Search Provider is available)
        # https://yandex.com/dev/maps/jsapi/doc/2.1/quick-start/index.html#get-api-key
        'provider.yandex.api_key': '',

        # misc
        'resources.root_path': LOCATION_FIELD_PATH,
        'resources.media': {
            'js': (
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
        'search.provider': 'nominatim',
    }

This will keep all other settings the same.
