Providers
=========

There are two kind of providers:

Map providers
-------------

Map providers are used to define the tile layers displayed on the map.

For this we have at first three options for predefined tile servers:

- `Google <providers.html#google>`__
- `Mapbox <providers.html#mapbox>`__
- `OpenStreetMap <providers.html#openstreetmap>`__

To set the map provider, use the ``map.provider`` property:

.. code-block:: python

    LOCATION_FIELD = {
        'map.provider': 'google',
    }

As there are many `tile servers <https://wiki.openstreetmap.org/wiki/Tiles#Servers>`__,
you can also set a custom one by defining a dict with at least the ``url`` property:

.. code-block:: python

    LOCATION_FIELD = {
        'map.provider': {
            'url': 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png',
            'options': {
                'maxZoom': '20',
            },
        },
    }


Search providers
----------------

Search providers are used to translate addresses into latitude and longitude.

For this we only have two option to offer for now:

- `Google <providers.html#google>`__
- `Yandex <https://tech.yandex.com/maps/geocoder/>`__
- `Nominatim <https://wiki.openstreetmap.org/wiki/Nominatim>`__

To set the search provider, use the ``search.provider`` property:

.. code-block:: python

    LOCATION_FIELD = {
        'search.provider': 'google',
    }


Google
------

If you are going to use **Google** as a map or search provider, you may want to
put your own credentials. You can even specify the map type:

.. code-block:: python

    LOCATION_FIELD = {
        'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
        'provider.google.api_key': '',
        'provider.google.api_libraries': '',
        'provider.google.map.type': 'ROADMAP',
    }


Mapbox
------

If you are going to use **Mapbox** as a map provider, you have to add your own
credentials:

.. code-block:: python

    LOCATION_FIELD = {
        'provider.mapbox.access_token': '',
        'provider.mapbox.max_zoom': 18,
        'provider.mapbox.id': 'mapbox.streets',
    }


OpenStreetMap
-------------

For now, the only setting available for **OpenStreetMap** is the ``max_zoom``:

.. code-block:: python

    LOCATION_FIELD = {
        'provider.openstreetmap.max_zoom': 18,
    }
