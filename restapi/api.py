from tastypie.resources import ModelResource
from restapi.models import Endpoint, Team, Project, Environment, Status, Event
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class EndpointResource(ModelResource):
    class Meta:
        queryset = Endpoint.objects.all()
        resource_name = 'endpoints'
        authorization= Authorization()
        always_return_data = True

        ordering = ['development', '-development']
        filtering = {
            'development': ALL_WITH_RELATIONS,
            'staging': ALL_WITH_RELATIONS,
            'integration': ALL_WITH_RELATIONS,
            'preproduction': ALL_WITH_RELATIONS,
            'production': ALL_WITH_RELATIONS,
        }

class TeamResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        resource_name = 'teams'
        authorization= Authorization()
        always_return_data = True

        ordering = ['creation_date', '-creation_date', "name", "-name"]

        filtering = {
            'name': ALL_WITH_RELATIONS,
            'description': ALL_WITH_RELATIONS,
            'email': ALL_WITH_RELATIONS,
            'manager': ALL_WITH_RELATIONS,
            'slackroom': ALL_WITH_RELATIONS,
        }

class ProjectResource(ModelResource):
    team = fields.ForeignKey(TeamResource, 'team', full=True)
    # self-referential foreign keys
    dependecies_downstream = fields.ToManyField('self', 'project_self_referential_on_fk', null=True)
    dependecies_upstream = fields.ToManyField('self', 'project_self_referential_by_fk', null=True)
    endpoint = fields.ForeignKey(EndpointResource, 'endpoint', null=True, full=True)
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'
        authorization= Authorization()
        always_return_data = True

        ordering = ['creation_date', '-creation_date', "name", "-name"]

        filtering = {
            'name': ALL_WITH_RELATIONS,
            'description': ALL_WITH_RELATIONS,
            'creation_date': ALL_WITH_RELATIONS,
            'git_repo': ALL_WITH_RELATIONS,
            'endpoint': ALL_WITH_RELATIONS,
            'team': ALL_WITH_RELATIONS,
            'dependecies_downstream': ALL_WITH_RELATIONS,
            'dependecies_upstream': ALL_WITH_RELATIONS,
            'endpoint_production': ALL_WITH_RELATIONS,
            'endpoint_staging': ALL_WITH_RELATIONS,
            'endpoint_dev':  ALL_WITH_RELATIONS,
        }

class EnvironmentResource(ModelResource):
    class Meta:
        queryset = Environment.objects.all()
        resource_name = 'environments'
        authorization= Authorization()
        always_return_data = True

        ordering = ['creation_date', '-creation_date', 'name', '-name']

        filtering = {
            'name': ALL_WITH_RELATIONS,
            'description': ALL_WITH_RELATIONS,
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
    project = fields.ForeignKey(ProjectResource, 'project', full=True)

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
            'deploy_ticket_url': ALL,
            'story_ticket_url': ALL,
            'release_tav': ALL,
            'project': ALL_WITH_RELATIONS,
        }

        ordering = ['date', '-date']
