from django.conf.urls.defaults import *

from inventory import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='inventory-list')
)
