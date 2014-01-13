try:
    from django.conf.urls import patterns
except ImportError:
    from django.conf.urls.defaults import patterns  # django < 1.4

import os

app_dir = os.path.dirname(__file__)

urlpatterns = patterns(
    '',
    (r'^media/(.*)$', 'django.views.static.serve', {
        'document_root': '%s/media' % app_dir}),
)
