# CrashCourse-Django
Rapid Prototyping with Django

## Overview

What you will learn

You will create your first Python/Django app, with basic CRUD (CReate, Update, Delete) functionality

Prerequisites
Ananconda - https://www.continuum.io/


Create a new virtual environment:
conda create -n djangocc django
::wait::

## Installation
### Mac
Python comes with macOS, so you can probably don't need to do anything other than confirm it is working. You can check this by typing ```python --version``` into Terminal. If Terminal prints something like Python 2.7.3 where the exact numbers you see may be different, you're all set! If you get an error message (or wish to have a different version than was included), you need to install and configure Python: 
- https://www.python.org/downloads/
- http://docs.python-guide.org/en/latest/starting/install3/osx/#install3-osx
- http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/
### Windows 
Windows doesn't come with any useful (non-Microsoft) development tools. So you will most definitly have to install Python.
https://www.howtogeek.com/197947/how-to-install-python-on-windows/

### Required Tools
#### Pip & SetupTools
There are a few package managers that are specific to Python, and pip is the preferred one. If you have Python 2 >=2.7.9 or Python 3 >=3.4 installed from python.org, you will already have pip and setuptools, but may need to upgrade to the latest version.

On Linux/MacOS:
```pip install -U pip setuptools```

On Windows:
```python -m pip install -U pip setuptools```

In the case you don't have pip or setuptools installed, the manual installation instructions are found here: https://pip.pypa.io/en/stable/installing/

tl;dr
```
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ python get-pip.py
```

#### VirtualEnv
```pip install virtualenv```

Django - https://www.djangoproject.com/ <br>

## Configuration
### Mac
### Windows
# Django Walkthrough

We are going to create an app that will create some To-Dos

create/update/blah blah

Some urls/functions

List
Create
Update
Delete



## Building a project skeleton
Lets create your first project:
Activate your virtual environment, goto your local code directory (like C:\Code, or  \user\Documents\code), and type:

django-admin startproject todo

```

 ───myproject
    │   manage.py
    │
    └───myproject
            settings.py
            urls.py
            wsgi.py
            __init__.py
```


From the Django Tutorial (https://docs.djangoproject.com/en/1.11/intro/tutorial01/):
- The outer myproject/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- manage.py: A command-line utility that lets you interact with this Django project in various ways.
- The inner myproject/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. myproject.urls).
- myproject/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
- myproject/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- myproject/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
- myproject/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

Ok, now we've created our Project Skeleton. Next, let's create our first application within the project

## Building your app skeleton
in the new /myproject/ directory, we'll tell django to create a new application.

python manage.py startapp todos

This will create the following structure

```
 ───todos
    │   admin.py
    │   apps.py
    │   models.py
    │   tests.py
    │   views.py
    │   __init__.py
    │
    └───migrations
            __init__.py
```


## Views
Let's your create first view

todos/views.py
```
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

```

## URLS
To make things more managable and sane, let's separate application urls from each other.

Create a new file urls.py in your todos directory

todos/urls.py
```

```



## Models

Defining your models

A model is the single, definitive source of truth about your data. It contains the essential fields and behaviors of the data you’re storing


in the /todos/models.py file, lets define our models.
```
from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user =  models.ForeignKey(User, unique=True)
    description = models.CharField(max_length=128, null=False, blank=False)
    due_State = models.DateField(null=True, blank=True)
```


Let's include the app we've just built into the project.

edit your myproject/settings.py file to include your new application:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todos.apps.TodosConfig'
]
```


## Forms
## Views
### Class based
### Function based
## Templates

Bootstrap.

## Tests
## Django Admin
## Running the CLI
### Migrations
### Shell
### HTTP Server
### Tests


### Next Steps

Django Plugins

django-extentions
django-modelutils
django-crispyforms

Make your stuff pretty
Bootstrap


