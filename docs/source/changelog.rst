*********
Changelog
*********

Versions
========

2.7.3
-----

- fix: removed console.log calls (#176)
- doc: documented how to release a new version

2.7.2
-----

- fix: 🐛 fix nominatim address search (#173)

2.7.1
-----

- fix: Remove reference to missing source map file (#168)


2.7.0
-----

**This is the last version to support Python 2.7**

- feat: Upgraded to leaflet 1.9.3 `PR <https://github.com/caioariede/django-location-field/pull/157>`_
- chore: New CI setup using GitHub Actions
- chore: Codebase now is formatted with black and isort


2.1.1
-----

- Fixed initial map rendering #84


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
