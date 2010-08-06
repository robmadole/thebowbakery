from django.conf.urls.defaults import *

from skin import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='skin-components'),
)
