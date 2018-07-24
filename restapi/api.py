from tastypie.resources import ModelResource
from restapi.models import Project, Environment, Status, Event
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'
        authorization= Authorization()
        always_return_data = True
        dependent_on = fields.ToManyField('restapi.api.ProjectResource', 'project_dependent_on_fk')
        dependent_by = fields.ToManyField('restapi.api.ProjectResource', 'project_dependent_by_fk')

        ordering = ['creation_date', '-creation_date', "name", "-name"]

        filtering = {
            'name': ALL_WITH_RELATIONS,
            'description': ALL_WITH_RELATIONS,
            'creation_date': ALL_WITH_RELATIONS,
            'git_repo': ALL_WITH_RELATIONS,
            'sprint_team': ALL_WITH_RELATIONS,
            'dependent_on': ALL_WITH_RELATIONS,
            'dependent_by': ALL_WITH_RELATIONS,
        }


class EnvironmentResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project', full=True)
    class Meta:
        queryset = Environment.objects.all()
        resource_name = 'environments'
        authorization= Authorization()
        always_return_data = True

        ordering = ['creation_date', '-creation_date', 'name', '-name']

        filtering = {
            'name': ALL_WITH_RELATIONS,
            'description': ALL_WITH_RELATIONS,
            'project': ALL_WITH_RELATIONS,
            'creation_date': ALL_WITH_RELATIONS,
        }

class StatusResource(ModelResource):
    class Meta:
        queryset = Status.objects.all()
        resource_name = 'statuses'
        authorization= Authorization()
        always_return_data = True

        filtering = {
            'name': ALL_WITH_RELATIONS,
            'description': ALL_WITH_RELATIONS,
        }

class EventResource(ModelResource):
    environment = fields.ForeignKey(EnvironmentResource, 'environment', full=True)
    status = fields.ForeignKey(StatusResource, 'status', null=True, blank=True)

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        authorization= Authorization()
        always_return_data = True

        filtering = {
            'date': ALL,
            'subject': ALL,
            'message': ALL,
            'status': ALL,
            'environment': ALL_WITH_RELATIONS,
            'release_version': ALL,
            'previous_version': ALL,
            'release_tav': ALL,
        }

        ordering = ['date', '-date']
