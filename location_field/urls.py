from django.conf.urls.defaults import *

import os

app_dir = os.path.dirname(__file__)

urlpatterns = patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/media' % app_dir}),
)
