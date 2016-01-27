*********
Changelog
*********

Versions
========

2.0.0
-----

- Added support to multiple map providers (Google, Mapbox, OpenStreetMap)
- Refactored the Javascript code to use `Leaflet.js <http://leafletjs.com/>`_


Upgrading
=========

From 1.x to 2.x
---------------

Backward incompatible changes
"""""""""""""""""""""""""""""

- Form fields no longer accepts the ``default`` parameter. If you are using
  them directly, without the model field, you have to replace the ``default``
  parameter by the well known standard parameter ``initial``.
- The ``based_fields`` parameter of model fields now only expects field names
  as strings and not field instances.
