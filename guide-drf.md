


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