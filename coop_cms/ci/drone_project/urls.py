# -*- coding: utf-8 -*-
"""urls"""

import sys

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.views import serve as serve_static
from django.views.static import serve as serve_media

from coop_cms.settings import get_url_patterns

localized_patterns = get_url_patterns()

admin.autodiscover()

urlpatterns = localized_patterns(
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('coop_cms.apps.email_auth.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)

if settings.DEBUG or ('test' in sys.argv) or getattr(settings, 'SERVE_STATIC', True):
    if settings.DEBUG:
        urlpatterns += [
            url(r'^static/(?P<path>.*)$', serve_static),
        ]
    else:
        urlpatterns += [
            url(r'^static/(?P<path>.*)$', serve_media, {'document_root': settings.STATIC_ROOT}),
        ]
    urlpatterns += [
        url(
            r'^media/(?P<path>.*)$',
            serve_media,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    ]
    
urlpatterns += localized_patterns(
    url(r'^djaloha/', include('djaloha.urls')),
    url(r'^', include('coop_cms.urls')),
    url(r'^coop_bar/', include('coop_bar.urls')),
)
