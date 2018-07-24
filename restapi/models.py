from django.db import models
import datetime

# https://books.agiliq.com/projects/django-orm-cookbook/en/latest/self_fk.html
# http://www.yodiaditya.com/django-tastypie-one-to-many-fields-related-models-reverse-backward/
class Project(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()
    git_repo = models.TextField()
    sprint_team = models.TextField()
    project_dependent_on = models.ForeignKey('self', on_delete=models.CASCADE, related_name='project_dependent_on_fk')
    project_dependent_by = models.ForeignKey('self', on_delete=models.CASCADE, related_name='project_dependent_by_fk')

    def __unicode__(self):
        return self.name

class Environment(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name = 'environments', on_delete=models.CASCADE)

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
    release_tag = models.TextField()
    environment = models.ForeignKey(Environment, related_name = 'events', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, blank=True, null=True, related_name = 'events', on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s (%s)" % (self.subject, self.message)
