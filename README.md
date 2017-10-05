# django-api


[![Build Status](https://travis-ci.org/NetoDevel/django-api.svg?branch=master)](https://travis-ci.org/NetoDevel/django-api)
[![Coverage Status](https://coveralls.io/repos/github/NetoDevel/django-api/badge.svg?branch=master)](https://coveralls.io/github/NetoDevel/django-api?branch=master)

# Requeriments

* Django
* djangorestframework
* django-cors-headers
* psycopg2
* pytz

# Usage
### if you use docker, run:
```
docker-compose build
docker-compose up

docker-compose run api python manage.py migrate
```
### for users without docker:

Application AngularJS
```
cd edge-app/
ng server
```

API Django

```
cd edge
./manage.py runserver
```

run tests
```
./manage.py test
```
