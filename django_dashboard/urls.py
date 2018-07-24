#from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from django.conf.urls  import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from restapi.api import EndpointResource, TeamResource, ProjectResource, EnvironmentResource, EventResource, StatusResource

v1_api = Api(api_name='v1')
v1_api.register(EndpointResource())
v1_api.register(TeamResource())
v1_api.register(ProjectResource())
v1_api.register(EnvironmentResource())
v1_api.register(EventResource())
v1_api.register(StatusResource())

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_dashboard.views.home', name='home'),
    # url(r'^django_dashboard/', include('django_dashboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^api/', include(v1_api.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]
