from django.db import models
import datetime

class ScalaProject(models.Model):

    def __str__(self):
       return self.name


class Endpoint(models.Model):
    """
    defines application endpoint information
    environment specific details to connect to an endpoint
    """
    name = models.CharField(max_length=255)
    development = models.CharField(max_length=255)
    staging = models.CharField(max_length=255)
    integration = models.CharField(max_length=255)
    preproduction = models.CharField(max_length=255)
    production = models.CharField(max_length=255)

    def __str__(self):
       return self.name

class Team(models.Model):
    """
    defines an dev team associated with a ProjectResource
    """
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    team_lead = models.CharField(max_length=200)
    senior_contact = models.CharField(max_length=200)
    slackroom = models.CharField(max_length=200)

    def __str__(self):
       return "{} by {}".format(self.name, self.manager)

class Platform(models.Model):
    """
    defines a platform a ProjectResource lives on
    examples: aws lambda, ec2, rackspace VM, rackspace physical, azure
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s" % (self.name)

class Project(models.Model):
    """
    defines an project resource and dependecies
    """
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()
    git_repo = models.URLField()
    endpoint = models.ForeignKey(Endpoint, null=True, related_name='endpoints', on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, null=True, related_name = 'platforms', on_delete=models.CASCADE)
    project_dependent_on = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='project_self_referential_on_fk')
    project_dependent_by = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='project_self_referential_by_fk')
    team = models.ForeignKey(Team, related_name = 'teams', on_delete=models.CASCADE)

    def __str__(self):
       return self.name

class Environment(models.Model):
    """
    defines a project environment such as dev, staging, prod
    """
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s" % (self.name)

class Status(models.Model):
    """
    defines a release status
    such as deployed, in test, pending deployment, draft
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ReleaseType(models.Model):
    """
    defines a release type such as config change, security patch,
    feature deployment, bugfix, etc
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Release(models.Model):
    """
    defines a release, this is a log to track releases and their status, purpose
    origns, stories, and deployment tickets
    """
    date = models.DateTimeField(default=datetime.datetime.now)
    headline = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    version_buildmap_tag = models.CharField(max_length=100, blank=True, null=True)
    version_released = models.CharField(max_length=16, blank=True)
    version_previous = models.CharField(max_length=16, blank=True)
    version_tag = models.CharField(max_length=100, blank=True)
    ticket_deploy_url = models.URLField()
    ticket_story_url = models.URLField(blank=True)
    project = models.ForeignKey(Project, related_name = 'projects', on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, related_name = 'environments', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name = 'statuses', on_delete=models.CASCADE)
    releasetype = models.ForeignKey(ReleaseType, related_name = 'releasetypes', on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s %s" % (self.project, self.environment, self.status, self.version_released)
