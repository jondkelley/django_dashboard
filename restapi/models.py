from django.db import models
import datetime


class Endpoint(models.Model):
    name = models.TextField()
    development = models.TextField()
    staging = models.TextField()
    integration = models.TextField()
    preproduction = models.TextField()
    production = models.TextField()

    def __str__(self):
       return self.name

class Team(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.TextField()
    manager = models.TextField()
    slackroom = models.TextField()

    def __str__(self):
       return "{} by {}".format(self.name, self.manager)

class Project(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()
    git_repo = models.URLField()
    endpoint = models.ForeignKey(Endpoint, null=True, related_name='endpoints', on_delete=models.CASCADE)
    project_dependent_on = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='project_self_referential_on_fk')
    project_dependent_by = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='project_self_referential_by_fk')
    team = models.ForeignKey(Team, related_name = 'teams', on_delete=models.CASCADE)

    def __str__(self):
       return self.name

class Environment(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return "%s" % (self.name)

class Status(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    headline = models.CharField(max_length=200)
    message = models.TextField()
    version_buildmap_tag = models.TextField(blank=True, null=True)
    version_released = models.TextField()
    version_previous = models.TextField()
    version_tag = models.TextField()
    ticket_deploy_url = models.URLField()
    ticket_story_url = models.URLField()
    project = models.ForeignKey(Project, related_name = 'environments', on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, related_name = 'events', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, blank=True, null=True, related_name = 'events', on_delete=models.CASCADE)

    def __str__(self):
        return "%s Version: %s %s" % (self.project, self.version_released, self.status)
