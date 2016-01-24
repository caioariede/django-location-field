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

- Starting in the 2.x version, the form fields do not accept the ``default``
  parameter anymore. If you are using them directly, without the model field,
  you have to replace the ``default`` parameter by the well known standard
  parameter ``initial``.
