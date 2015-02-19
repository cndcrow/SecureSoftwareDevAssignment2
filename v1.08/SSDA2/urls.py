from django.conf.urls import patterns, include, url
from SSDA2.views import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SSDA2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', curr_date),
    url(r'^testapp/', include('testapp.urls')),
)
