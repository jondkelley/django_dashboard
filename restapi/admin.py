from django.contrib import admin
from restapi.models import Project, Environment, Status, Event, Endpoint, Team

admin.site.register(Project)
admin.site.register(Environment)
admin.site.register(Status)
admin.site.register(Event)
admin.site.register(Endpoint)
admin.site.register(Team)
