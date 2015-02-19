from django.conf.urls import patterns, url
from testapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^register/$', views.addUser, name='register'),
)