from django.conf.urls import patterns, include, url
from django.contrib import admin
from lupine import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warbird.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^callback', views.callback, name="callback"),
    url(r'^accounts/', include('registration.urls')),
    url(r'^lupine/', include('lupine.urls'))
)
