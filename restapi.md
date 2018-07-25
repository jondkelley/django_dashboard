### Authentication/Authorization

You will need to use the django admin at /admin/ to configure an API user. For requests to this API you will need to add the HTTP header Authorization: ApiKey user_here:api_key_here

## Team

A team will describe a dev team who writes code for a project.

* List all teams:

`GET http://.../api/teams`


* List all specific team:

`GET http://.../api/teams/{id}`

* Create a new team:

`POST http://.../api/teams`

With header: `Content-Type: application/json`   
With body:
`{
        "description": "This team deploys software.",
        "email": "bluebarracudas@company.com",
        "manager": "Mr Manager",
        "name": "Blue Barracudas",
        "senior_contact": "Escalation Guy",
        "slackroom": "#blue_barracudas",
        "team_lead": "Team Leader"
      }`

## Endpoint

An endpoint describes the resources in different environments. This can be done better with foreign keys against the environment table, but fits most organizational purposes.

* List all teams:

`GET http://.../api/endpoints`


* List all specific team:

`GET http://.../api/endpoints/{id}`

* Create a new team:

`POST http://.../api/endpoints`

With header: `Content-Type: application/json`   
With body:
`{
        "development": "http://192.168.100.10:8080",
        "integration": "http://192.168.200.10:4737",
        "name": "productname_endpoints",
        "preproduction": "http://192.168.300.10:3822",
        "production": "http://192.168.400.10:2382",
        "staging": "http://192.168.9.10:11"
      }`


## Platform

A platform describes the underlying infrastructure platform for a project. This could be something like Amazon EC2, Amazon ECS, Rackspace Cloud, VMWare Esxi, Azure, or Heroku.

* List all teams:

`GET http://.../api/platforms`


* List all specific team:

`GET http://.../api/platforms/{id}`

* Create a new team:

`POST http://.../api/platforms`

With header: `Content-Type: application/json`   
With body:
`{
        "description": "Our ECS Cluster",
        "name": "Amazon ECS"
      }`

###Project

A Project describes the actual software project your teams create.  
A Project is run/tested/experienced on several Environments on a single platform.
If you have a slew of dependent projects, you can reference them as a list.

* List all projects

`GET http://.../api/projects`

* Return a specific project:

`GET http://.../api/projects/{id}`

* Create a new project:

`POST http://.../api/projects`

With header: `Content-Type: application/json`   
With body:
`{
  "dependecies_downstream": [
    "/api/v1/projects/1",
    "/api/v1/projects/2"
  ],
  "dependecies_upstream": [
    "/api/v1/projects/2"
  ],
  "description": "Project Description",
  "endpoint": "/api/v1/endpoints/{id}"
  "git_repo": "https://github.com/BoomTownROI/haproxy_api/tree/master/hapee_api"
  "name": "haproxy_api_crm",
  "platform": "/api/v1/platforms/{id}",
  "team": "/api/v1/teams/{id}"
}`

* Updates and returns a project

`PUT http://.../api/projects/{id}`

With header: `Content-Type: application/json`   
With body:
`{
 "name" : {string},
 "description" : {string}
}`

* Delete a project (and associated resources!)

`DELETE http://.../api/projects/{id}`

###Environment
An Environment is where a Project is run/tested/experienced.   
There can be several different Environment for the same Project.

* List all environments

`GET http://.../api/environments`

* List all environments for a specific project

`GET http://.../api/environments?project={id}`

* Return a specific environment

`GET http://.../api/environments/{id}`

* Create a new environment

`POST http://.../api/environments`

With header: `Content-Type: application/json`   
With body:
`{
  "description": "",
  "name": "PRODUCTION",
}`

* Updates and returns an environment

`PUT http://.../api/environments/{id}`

With header: `Content-Type: application/json`   
With body:
`ent-Type: application/json`   
With body:
`{
  "description": "New Description",
  "name": "PRODUCTION",
}`

* Delete an environment (and associated resources!)

`DELETE http://.../api/environments/{id}`

###Release
An Release is something that may happen in the life of a project.

* List all events

`GET http://.../api/releases`

* List all events for a specific environment

`GET http://.../api/releases?environment={id}`

* List all events for a specific project name

`GET http://.../api/releases?project__name={name}`

* Create a new event

`POST http://.../api/events`

With header: `Content-Type: application/json`   
With body:
`{
      "environment": "/api/v1/environments/1",
      "headline": "New feature X!",
      "message": "",
      "project": "/api/v1/projects/2",
      "releasetype": "/api/v1/releasetypes/5",
      "resource_uri": "/api/v1/releases/2",
      "status": "/api/v1/statuses/1",
      "ticket_deploy_url": "http://jira.com/OPS-43",
      "ticket_story_url": "",
      "version_buildmap_tag": null,
      "version_previous": "1.2.2",
      "version_released": "1.2.3",
      "version_tag": ""
    }`

###Status
A Status is an optional parameter to describe an Event.

* List all statuses

`GET http://.../api/statuses`

* Return a specific status

`GET http://.../api/statuses/{id}`

* Create a new status

`POST http://.../api/statuses`

With header: `Content-Type: application/json`   
with body:
`{
  "description": "",
  "name": "RELEASED",
}`

* Updates and returns a status

`PUT http://.../api/status/{id}`

With header: `Content-Type: application/json`   
With body:
`{
  "description": {string},
  "name": {string},
}`

* Delete a status (and associated resources!)

`DELETE http://.../api/statuses/{id}`
