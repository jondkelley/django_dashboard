from django.db import models
import datetime


class Team(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.TextField()
    manager = models.TextField()
    slackroom = models.TextField()

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.project)

class Project(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()
    git_repo = models.URLField()
    endpoint_dev = models.TextField()
    endpoint_staging = models.TextField()
    endpoint_production = models.TextField()
    project_dependent_on = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='project_self_referential_on_fk')
    project_dependent_by = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='project_self_referential_by_fk')
    team = models.ForeignKey(Team, related_name = 'teams', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class Environment(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.project)

class Status(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Event(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    release_version = models.TextField()
    previous_version = models.TextField()
    deploy_ticket_url = models.URLField()
    story_ticket_url = models.URLField()
    release_tag = models.TextField()
    project = models.ForeignKey(Project, related_name = 'environments', on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, related_name = 'events', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, blank=True, null=True, related_name = 'events', on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s (%s)" % (self.subject, self.message)
