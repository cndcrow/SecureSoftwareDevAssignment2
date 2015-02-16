from django.conf.urls import patterns, include, url
from SSDA2.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SSDA2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', curr_date),
    url(r'^time/plus(\d{1,2})/$', hours_ahead),
)
