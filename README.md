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
Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, rather than being installed globally. This is something you want to do almost 100% of the time. It is fast, easy, and most importantly it's safe. Currently, there are two viable tools for creating Python virtual environments:

**venv** is available by default in Python 3.4 and later, and installs **pip** and **setuptools** into created virtual environments in Python 3.4 and later.

Docs: https://docs.python.org/3/library/venv.html

```
python3 -m venv <DIR>
source <DIR>/bin/activate
```

**virtualenv** needs to be installed separately, but supports Python 2.6+ and Python 3.3+, and **pip**, **setuptools** and **wheel** are always installed into created virtual environments by default (regardless of Python version).

Docs: https://virtualenv.pypa.io/en/stable/

```
pip install virtualenv
virtualenv <DIR>
source <DIR>/bin/activate
```


*NOTE: Your prompt will change after activating a virtual environemnt. This will let you know you did thing correctly, as well as help identify which environment is active.*

# Django Walkthrough
Django - https://www.djangoproject.com/
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
$(danjo-env) pip install django
```

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





