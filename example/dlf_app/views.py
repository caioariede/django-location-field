from django.views.generic import CreateView

from .models import Place


class PlaceCreateView(CreateView):
    model = Place
    fields = (
        'parent_place',
        'city',
        'location',
    )
