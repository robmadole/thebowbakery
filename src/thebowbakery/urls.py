from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Redirects
    url(r'^$', 'django.views.generic.simple.redirect_to', {'url': 'bows/'}),

    # Our bow inventory, main display views
    url(r'^bows/', include('inventory.urls')),

    url(r'^admin/',
        include(admin.site.urls)),

    url(r'^grappelli/',
        include('grappelli.urls')),
)

if settings.DJANGO_SERVES_MEDIA:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
