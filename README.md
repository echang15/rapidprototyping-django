# CrashCourse-Django
Rapid Prototyping with Django

## Overview

You will create your first Python/Django app, with basic CRUD (Ceate, Read, Update, Delete) functionality. We will do this by building a simple todo application modeled after [todo-MVC](http://todomvc.com/)

What you will learn:

- How to get python up and running
- How to install python packages
- How to work with python virtual environments
- How to build a basic prototype using the [Django framework](https://www.djangoproject.com/)


## Python Installation
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

**tl;dr**
```
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ python get-pip.py
```

#### VirtualEnv
Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, rather than being installed globally. This is something you want to do almost 100% of the time. It is fast, easy, and most importantly it's safe. Currently, there are two viable tools for creating Python virtual environments:

**venv** - this is available by default in Python 3.4 and later, and installs **pip** and **setuptools** into created virtual environments in Python 3.4 and later.

Docs: https://docs.python.org/3/library/venv.html

```
python3 -m venv <DIR>
source <DIR>/bin/activate
```

**virtualenv** - this needs to be installed separately, but supports Python 2.6+ and Python 3.3+, and **pip**, **setuptools** and **wheel** are always installed into created virtual environments by default (regardless of Python version).

Docs: https://virtualenv.pypa.io/en/stable/

```
pip install virtualenv
virtualenv <DIR>
source <DIR>/bin/activate
```


*NOTE: Your prompt will change after activating a virtual environemnt. This will let you know you did thing correctly, as well as help identify which environment is active.*

# Django Walkthrough
We are going to create an app that will create some To-Dos. This is a very abrieiated tutorial that is tailored for our example application, and does not cover all of Django at great depth. For that, you should walk though the [offical documentation](https://docs.djangoproject.com/en/1.11/) and [tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/).

For our application, we need a way to create, view, update, and delete todos. As a strech goal, we would like the ability to have different people login and be able to work with only the todos that belong to them. 

## Ready your environment
### Create a django virtual environment
This assumes you are using Python 2.7+ and the **virtualenv** tool. For Python 3.4+, please see above instructions for **venv**.
```
virtualenv /path/to/my/environments/django-env
```

On Linux/macOS:
```
virtualenv /path/to/my/environments/django-env
source /path/to/my/environments/django-env/bin/activate
```

On Windows:
```
virtualenv c:\path\to\my\environments\django-env
c:\path\to\my\environments\django-env\Scripts\activate.bat
```


## Install your dependancies
You will need the **django** package at a bare minimum, so lets install that into our virtual environment. We will install other packages later as nessisary.

```
(danjo-env)$ pip install django
```


## Building a project skeleton
Lets create your first project:

```django-admin startproject todo```

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
In the new /myproject/ directory, we'll tell django to create a new application.

```python manage.py startapp todos```

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
    return HttpResponse("Hello, world. You're at the todo index.")
```



## URLS
To make things more managable and sane, let's separate application urls from each other.

Create a new file urls.py in your todos directory

todos/urls.py
```
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/create/$', views.create, name='create')
    url(r'^(?P<id>+)/$', views.detail, name='detail')
    url(r'^(?P<id>+)/update/$', views.update, name='update')
    url(r'^(?P<id>+)/delete/$', views.delete, name='delete')
]
```

Now we need to tell the project's URL's file to look for the todo app's specific urls...

myproject/urls.py
```
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('todos.urls')),
    url(r'^admin/', admin.site.urls),
]

```


## Tests

Lets start our first test.


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
    due_date = models.DateField(null=True, blank=True)
```


```python manage.py makemigrations```
```python manage.py migrate```


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
``` python manage.py createsuperuser ```
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


