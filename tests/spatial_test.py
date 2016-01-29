from django.test import TestCase
from django.contrib.gis.geos import Point

from tests.spatial_models import SpatialPlace


class LocationFieldSpatialTest(TestCase):
    def test_spatial(self):
        vals = {
            'city': 'Bauru',
            'location': 'POINT(-22.2878573 -49.0905487)',
        }

        obj = SpatialPlace.objects.create(**vals)

        self.assertEqual(obj.city, 'Bauru')
        self.assertEqual(obj.location, Point(-22.2878573, -49.0905487))
