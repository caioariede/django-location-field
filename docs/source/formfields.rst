***********
Form fields
***********

There are two type of form fields, the ``PlainLocationField`` `for non-spatial
databases <#for-non-spatial-databases>`__ and the ``LocationField`` `for
spatial databases <#for-spatial-databases>`__ like PostGIS and SpatiaLite.

The attributes that can be passed to both form fields are:

============ ===========
Attribute    Description
============ ===========
based_fields A list of fields that will be used to populate the location field
zoom         The default zoom level for the map
suffix       A suffix that will be added to the search string, like a city
             name. Useful when you want to restrict the search to determined
             areas.
============ ===========


For non-spatial databases
-------------------------

For non-spatial databases you may want to use the ``PlainLocationField``,
which stores the latitude and longitude values as plain text.

Example:

.. code-block:: python

    from django import forms
    from location_field.forms.plain import PlainLocationField

    class Address(forms.Form):
        city = forms.CharField()
        location = PlainLocationField(based_fields=['city'],
                                      initial='-22.2876834,-49.1607606')


For spatial databases
---------------------

For spatial databases like ``PostGIS`` and ``SpatiaLite`` you may want to use
the ``LocationField``, which stores the latitude and longitude values as a
`Point <https://docs.djangoproject.com/en/dev/ref/contrib/gis/geos/#point>`_
object.

Example:


.. code-block:: python

    from django import forms
    from django.contrib.gis.geos import Point

    from location_field.forms.plain import PlainLocationField


    class Address(forms.Form):
        city = forms.CharField()
        location = LocationField(based_fields=['city'],
                                 initial=Point(-49.1607606, -22.2876834))
