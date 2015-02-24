__author__ = 'harshit'
from django.conf.urls import include, patterns, url
from lupine import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warbird.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="index"),
    url(r'^callback', views.callback, name="callback"),
    url(r'^clean', views.clean, name="clean"),
    url(r'^webhooks', views.hooks, name="hooks"),
    url(r'^payload', views.payload, name="payload"),
)
