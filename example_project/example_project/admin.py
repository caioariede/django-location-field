from django.contrib import admin

from .models import Chain, Place


class PlaceInline(admin.TabularInline):
    model = Place


class ChainAdmin(admin.ModelAdmin):
    inlines = [
        PlaceInline,
    ]


admin.site.register(Chain, ChainAdmin)
