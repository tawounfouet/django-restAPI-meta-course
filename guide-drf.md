


## Testing first request using insomnia

```bash

#
# GET http://httpbin.org/get?project=LitteLemon



## Setting Up Environment

```bash
# Create a virtual environment using Pipenv

pipenv lock 
pipenv install django 
pipenv install djangorestframework
#pipenv install djangorestframework django-cors-headers


# Activate the virtual environment
pipenv shell

# Start a new Django project
django-admin startproject BookList .

# Create a new app
python manage.py startapp BookListAPI

# Adding the django debug toolbar to the project
pipenv install django-debug-toolbar

# Add the app to the INSTALLED_APPS list in settings.py
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'debug_toolbar',
    'BookListAPI',
]

# Add the following to the end of the settings.py file
# This will allow us to use the debug toolbar when we are in debug mode
if DEBUG:
    import debug_toolbar
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True
    }
```



## Create a simple endpoint

```python
# BookListAPI/views.py
import json
from django.http import HttpResponse

def index(request):
    return HttpResponse(json.dumps({'message': 'Hello, world!'}), content_type='application/json')


# using decorator @api_view()

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def index(request):
    return Response({'message': 'Hello, world!'})

@api_view()
def books(request):
    books = [
        {'id': 1, 'title': 'Book 1'},
        {'id': 2, 'title': 'Book 2'},
    ]
    return Response('List of books', books, status=status.HTTP_200_OK)

```


## Restaurant menu API project with DRF

```bash
# Create a new App called LittleLemonAPI
python manage.py startapp LittleLemonAPI

```

```bash
# Renderers

# JSONRenderer
rest_framework.renderers.JSONRenderer

# BrowsableAPIRenderer
rest_framework.renderers.BrowsableAPIRenderer


# XMLRenderer
pipenv djangorestframework-xml # installation 
rest_framework_xml.renderers.XMLRenderer


# Headers
Content-Type: application/json
Accept: application/json

# GET http:


# 
```