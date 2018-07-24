from tastypie.resources import ModelResource
from restapi.models import Endpoint, Team, Project, Platform, Environment, Status, Release, ReleaseType
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

#
class EndpointResource(ModelResource):
    """
    defines application endpoint information
    environment specific details to connect to an endpoint
    """
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
    """
    defines an dev team associated with a ProjectResource
    """
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
            'team_lead': ALL_WITH_RELATIONS,
            'senior_contact': ALL_WITH_RELATIONS,
            'slackroom': ALL_WITH_RELATIONS,
        }

class PlatformResource(ModelResource):
    """
    defines a platform a ProjectResource lives on
    examples: aws lambda, ec2, rackspace VM, rackspace physical, azure
    """
    class Meta:
        queryset = Platform.objects.all()
        resource_name = 'platforms'
        authorization= Authorization()
        always_return_data = True

        ordering = ['name', '-name']

        filtering = {
            'name': ALL_WITH_RELATIONS,
            'description': ALL_WITH_RELATIONS,
        }

class ProjectResource(ModelResource):
    """
    defines an project resource and dependecies
    """
    team = fields.ForeignKey(TeamResource, 'team', full=True)
    # self-referential foreign keys
    dependecies_downstream = fields.ToManyField('self', 'project_self_referential_on_fk', null=True)
    dependecies_upstream = fields.ToManyField('self', 'project_self_referential_by_fk', null=True)
    platform = fields.ForeignKey(PlatformResource, 'platform', null=True, full=True)
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
            'platform': ALL_WITH_RELATIONS,
            'team': ALL_WITH_RELATIONS,
            'dependecies_downstream': ALL_WITH_RELATIONS,
            'dependecies_upstream': ALL_WITH_RELATIONS,
            'endpoint_production': ALL_WITH_RELATIONS,
            'endpoint_staging': ALL_WITH_RELATIONS,
            'endpoint_dev':  ALL_WITH_RELATIONS,
        }

class EnvironmentResource(ModelResource):
    """
    defines a project environment such as dev, staging, prod
    """
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
    """
    defines a release status
    such as deployed, in test, pending deployment, draft
    """
    class Meta:
        queryset = Status.objects.all()
        resource_name = 'statuses'
        authorization= Authorization()
        always_return_data = True

        filtering = {
            'name': ALL_WITH_RELATIONS,
            'description': ALL_WITH_RELATIONS,
        }

class ReleaseTypeResource(ModelResource):
    """
    defines a release type such as config change, security patch,
    feature deployment, bugfix, etc
    """
    class Meta:
        queryset = ReleaseType.objects.all()
        resource_name = 'releasetypes'
        authorization= Authorization()
        always_return_data = True

        ordering = ['name', '-name']
        filtering = {
            'name': ALL_WITH_RELATIONS,
            'description': ALL_WITH_RELATIONS
        }

class ReleaseResource(ModelResource):
    """
    defines a release, this is a log to track releases and their status, purpose
    origns, stories, and deployment tickets
    """
    environment = fields.ForeignKey(EnvironmentResource, 'environment', full=True)
    status = fields.ForeignKey(StatusResource, 'status', null=True, blank=True)
    project = fields.ForeignKey(ProjectResource, 'project', full=True)
    releasetype = fields.ForeignKey(ReleaseTypeResource, 'releasetype', full=True)

    class Meta:
        queryset = Release.objects.all()
        resource_name = 'releases'
        authorization= Authorization()
        always_return_data = True

        filtering = {
            'date': ALL,
            'headline': ALL,
            'message': ALL,
            'status': ALL,
            'environment': ALL_WITH_RELATIONS,
            'version_buildmap_tag': ALL,
            'version_released': ALL,
            'version_previous': ALL,
            'version_tag': ALL,
            'ticket_deploy_url': ALL,
            'ticket_story_url': ALL,
            'project': ALL_WITH_RELATIONS,
        }

        ordering = ['date', '-date']
