from django.test import TestCase
from django.contrib.gis.geos import Point

from tests.models import Place, SpatialPlace


class LocationFieldTest(TestCase):
    def test_plain(self):
        vals = {
            'city': 'Bauru',
            'location': '-22.2878573,-49.0905487',
        }

        obj = Place.objects.create(**vals)

        self.assertEqual(obj.city, 'Bauru')
        self.assertEqual(obj.location, '-22.2878573,-49.0905487')

    def test_spatial(self):
        vals = {
            'city': 'Bauru',
            'location': 'POINT(-22.2878573 -49.0905487)',
        }

        obj = SpatialPlace.objects.create(**vals)

        self.assertEqual(obj.city, 'Bauru')
        self.assertEqual(obj.location, Point(-22.2878573, -49.0905487))
