from django.contrib import admin
from restapi.models import Project, Platform, Environment, Status, ReleaseType, Release, Endpoint, Team

admin.site.register(Project)
admin.site.register(Platform)
admin.site.register(Environment)
admin.site.register(Status)
admin.site.register(ReleaseType)
admin.site.register(Release)
admin.site.register(Endpoint)
admin.site.register(Team)
