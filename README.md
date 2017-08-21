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
Python comes with macOS, so you can probably don't need to do anything other than confirm it is working. You can check this by typing ```python --version``` into Terminal. If you get an error message, you need to install Python. If Terminal prints something like Python 2.7.3 where the exact numbers you see may be different, you're all set!
http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/
### Windows 
https://www.howtogeek.com/197947/how-to-install-python-on-windows/

### Required Tools
#### SetupTools
#### Pip
There are a few package managers that are specific to Python, and pip is the preferred one. Install instruction are found here: https://pip.pypa.io/en/stable/installing/

tl;dr
```
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ python get-pip.py
```

#### VirtualEnv

Django - https://www.djangoproject.com/ <br>

## Configuration
### Mac
### Windows
# Django Walkthrough
## Building a project skeleton
Lets create your first project:
Activate your virtual environment, goto your local code directory (like C:\Code, or  \user\Documents\code), and type:

django-admin startproject todo

```
C:.
│   README.md
│
└───todo
    │   manage.py
    │
    └───todo
            settings.py
            urls.py
            wsgi.py
            __init__.py
```

## Building your app skeleton
## Models

in /models/todo.py, 
## Forms
## Views
### Class based
### Function based
## Templates
## Tests
## Django Admin
## Running the CLI
### Migrations
### Shell
### HTTP Server
### Tests





