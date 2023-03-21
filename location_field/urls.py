import os

from django.conf.urls import patterns

app_dir = os.path.dirname(__file__)

urlpatterns = patterns(
    "",
    (
        r"^media/(.*)$",
        "django.views.static.serve",
        {"document_root": "%s/media" % app_dir},
    ),
)
