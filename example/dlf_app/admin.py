from django.contrib import admin
from dlf_app.models import Place


class PlaceInline(admin.TabularInline):
    model = Place
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceInline,
    ]


admin.site.register(Place, PlaceAdmin)
