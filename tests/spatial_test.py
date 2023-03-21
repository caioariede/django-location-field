import pytest

@pytest.mark.spatial
@pytest.mark.django_db
def test_spatial(db):
    from django.contrib.gis.geos import Point
    from tests.models import SpatialPlace

    vals = {
        'city': 'Bauru',
        'location': 'POINT(-22.2878573 -49.0905487)',
    }

    obj = SpatialPlace.objects.create(**vals)

    assert obj.city == 'Bauru'
    assert obj.location == Point(-22.2878573, -49.0905487, srid=4326)
