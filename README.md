## REST API, based on django, to implement a Release Dashboard API for your dev team

The frontend is truly up to yourself, as the features and considerations of a frontend are very organization or company-specific considerations. You might also wish to integrate this tooling with your existing technology of choice.

This project provides a REST API to create/read/update/delete:
* Projects
* Environments
* Releases
* Statuses
* Endpoints
* Teams
* Platforms
* ReleaseTypes

Installation:
-------------
* Clone repository   
`git clone https://github.com/jondkelley/django_dashboard.git`
* cd into project directory   
`cd django_dashboard`
* Install requirements with pip   
`pip3.4 install -r requirements.txt`
* Prepare database and create django superadmin access   
`python3.4 manage.py makemigrations`
* Sync tables   
`python3.4 manage.py migrate`
* Create superuser
`python3.4 manage.py createsuperuser`
* Run server   
`python3.4 manage.py runserver`

REST API schema is then available at [http://localhost:8000/api/v1](http://localhost:8000/api/v1)

For a more traditional documentation you can read [restapi.md](https://github.com/jondkelley/oss_release_api/blob/master/restapi.md)
