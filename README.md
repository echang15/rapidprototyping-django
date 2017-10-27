# Rapid Prototyping with Django

## Overview

You will create your first Python/Django app, with basic CRUD (Create, Read, Update, Delete) functionality. We will do this by building a simple "To-do" application modeled after [todo-MVC](http://todomvc.com/)

What you will learn:

- How to get python up and running
- How to install python packages
- How to work with python virtual environments
- How to build a basic prototype using the [Django framework](https://www.djangoproject.com/)

What we will NOT cover:
- HTML/CSS/JS - There are plenty of other tutorials out there.


## Python Installation
### Mac
Python comes with macOS, so you can probably don't need to do anything other than confirm it is working. You can check this by typing ```python --version``` into Terminal. If Terminal prints something like Python 2.7.3 where the exact numbers you see may be different, you're all set! If you get an error message (or wish to have a different version than was included), you need to install and configure Python: 
- https://www.python.org/downloads/
- http://docs.python-guide.org/en/latest/starting/install3/osx/#install3-osx
- http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/
### Windows 
Windows doesn't come with any useful (non-Microsoft) development tools. So you will most definitely have to install Python.
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
```bash
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ python get-pip.py
```

#### VirtualEnv
Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, rather than being installed globally. This is something you want to do almost 100% of the time. It is fast, easy, and most importantly it's safe. Currently, there are two viable tools for creating Python virtual environments:

**venv** - this is available by default in Python 3.4 and later, and installs **pip** and **setuptools** into created virtual environments in Python 3.4 and later.

Docs: https://docs.python.org/3/library/venv.html

```bash
python3 -m venv <DIR>
source <DIR>/bin/activate
```

**virtualenv** - this needs to be installed separately, but supports Python 2.6+ and Python 3.3+, and **pip**, **setuptools** and **wheel** are always installed into created virtual environments by default (regardless of Python version).

Docs: https://virtualenv.pypa.io/en/stable/

```bash
pip install virtualenv
virtualenv <DIR>
source <DIR>/bin/activate
```


*NOTE: Your prompt will change after activating a virtual environment. This will let you know you did thing correctly, as well as help identify which environment is active.*

# Django Walk-through
We are going to create an application that will create some To-Dos. This is a very abbreviated tutorial that is tailored for our example application, and does not cover all of Django at great depth. For that, you should walk though the [official documentation](https://docs.djangoproject.com/en/1.11/) and [tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/).

For our application, we need a way to create, view, update, and delete todos. As a stretch goal, we would like the ability to have different people login and be able to work with only the todos that belong to them. 

## Ready your environment
### Create a django virtual environment
This assumes you are using Python 2.7+ and the **virtualenv** tool. For Python 3.4+, please see above instructions for **venv**.
```bash
virtualenv /path/to/my/environments/django-env
```

On Linux/macOS:
```bash
virtualenv /path/to/my/environments/django-env
source /path/to/my/environments/django-env/bin/activate
```

On Windows:
```bash
virtualenv c:\path\to\my\environments\django-env
c:\path\to\my\environments\django-env\Scripts\activate.bat
```


## Install your dependencies
You will need the **django** package at a bare minimum, so lets install that into our virtual environment. We will install other packages later as necessary.

```bash
(django-env)$ pip install django
```


## Building a project skeleton
Lets create your first project:

```django-admin startproject myproject```

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


Let's include the app we've just built into the project.

edit your `myproject/settings.py` file to include your new application:
```python
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


Add the following lines of code to the bottom of the ```settings.py``` file. These settings are implementing some extra security and overwrite some default settings to work with some of the code below. Check the Django documentation if you want to learn more about what these settings do.

```python
# Login redirection settings
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

# Security Settings
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```


## Templates
Let's work from the user up and start with creating an HTML template we want to display when people first visit our app. We will refer to this as the *home* or *index* template.

Before we create the html templates we have to create the directory structure where Django expects to find them. From the *todos* folder above to the following:

```bash
mkdir -p todos/templates/todos/
touch todos/templates/todos/index.html
```

Then create the following html file:  todos/templates/todos/index.html
```html
<html>
    <head></head>
    <body>This is the home page</body>
</html>
```

Your app folder should now look like this:

```
 ───todos
    │   admin.py
    │   apps.py
    │   models.py
    │   tests.py
    │   views.py
    │   __init__.py
    │
    └───templates
    |   └───todos
    |           index.html   
    └───migrations
            __init__.py
```



## Views
Now that we have the html template we want the users to see, let's your create first view that will use that template.

**todos/views.py**
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "todos/index.html")
```



## URLS
To make things more manageable, let's separate application level urls from project level ones.

Create a new file `urls.py` in your todos directory

**todos/urls.py**
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

Now we need to tell the project's URL's file to look for the todo app's specific urls...

**myproject/urls.py**
```python
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    url(r'^accounts/login/', LoginView.as_view(), name="user_login"),
    url(r'^accounts/logout/', LogoutView.as_view(), name="user_logout"),
    url(r'^accounts/register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('todos.urls')),
]

```

### Checking to see if everything works
Now that we've created our first views (views.py), hooked it into our router (urls.py), and template (index.html), lets try running our app.

```python manage.py runserver```

This will spin up a local server of your code. From your browser, goto the following url:
http://localhost:8000

You should see your rendered index.html file.


## Models

Defining your models

A model is the single, definitive source of truth about your data. It contains the essential fields and behaviors of the data you're storing. Each model is a Python class that subclasses `django.db.models.Model`. Each attribute of the model represents a database field. With all of this, Django gives you an automatically-generated database-access API; see https://docs.djangoproject.com/en/1.11/topics/db/queries/

In the `/todos/models.py` file, lets define our models.
```python
from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user =  models.ForeignKey(User, null=True, blank=True)
    description = models.CharField(max_length=128, null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description
```

### What are we doing?
We are telling django that we're creating a object called Todo. This model has 3 properties: user, description, and due_date, and they have attributes. For the description, we're telling django that the max length is 128 characters, and there must be a value there to pass validation.

Ok, we've defined our models, but we haven't created them in our database yet; lets do that.

```bash
python manage.py makemigrations todos
python manage.py migrate
```

Ok, what did we just do? We just told django to create a migration script that will analyze the current state of the DB, and script out the changes that need to happen in order to sync it with the current definition. Then, we executed the changes.

#### Why two steps instead of one?
the migration scripts can be copied across to other environments, so we can apply the changes to other copies of the application...


## Tests

Lets start our first test. 

**todos/tests.py**
```python
from django.test import TestCase
from django.test.client import Client

from .models import Todo


class TodoTests(TestCase):

    def setUp(self):
        """Lets create one todo that we can use within the tests below"""
        self.example_todo = Todo.objects.create(description="test")

    def test_model_fields_exist(self):
        self.assertTrue(Todo._meta.get_field('user'))
        self.assertTrue(Todo._meta.get_field('description'))
        self.assertTrue(Todo._meta.get_field('due_date'))
```

To run this test, type ```python manage.py test```
If this test passes, you know that you've created the todo model's fields.


### Why Test?
Because code inevitably changes and grows. As you add and modify features, you run tests against all your new and old code to make sure nothing is broken. Always test before pushing things up into higher environments, or into source code control!

### What to Test?
Any custom logic, such as form validations, view redirects, permission-based views, etc.

Ok, so we have a model now and have a basic test against it, how do we interact with it?


## Forms
### What is a Form?
From https://docs.djangoproject.com/en/1.11/topics/forms/ :
"In HTML, a form is a collection of elements inside <form>...</form> that allow a visitor to do things like enter text, select options, manipulate objects or controls, and so on, and then send that information back to the server." Django handles three distinct parts of the work involved in forms:

- preparing and restructuring data to make it ready for rendering
- creating HTML forms for the data
- receiving and processing submitted forms and data from the client

While there are ways to customize and extend forms to suit your own need, we won't cover that today. We will use Django's ModelForms, which is free and built-in. (https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/)



## Views

### Class based views

A view is simply a callable which takes a request and returns a response. This can be more than just a function, and Django provides a variety of generic classes which can be used as views. These allow you to structure your views and reuse code by harnessing inheritance and mixins. See: (https://docs.djangoproject.com/en/1.11/ref/class-based-views/)

So in our views.py, instead of hand crafting CRUD functions we can leverage the generic class based views to do the same thing in a very small amount of code:

```python
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from todos.models import Todo


class todo_list(ListView):
    ''' This will display a list of all the todos '''
    model = Todo


class todo_details(DetailView):
    ''' This will display a page with the details of a single todo '''
    model = Todo

# Require login for this view
@method_decorator(login_required, name='dispatch')
class todo_create(CreateView):
    ''' This will display a simple form and allow users to create a todo '''
    model = Todo
    fields = ['user', 'description', 'due_date']

    def get_success_url(self):
        return reverse('todo_details', kwargs={'pk': self.object.pk})

# Require login for this view
@method_decorator(login_required, name='dispatch')
class todo_update(UpdateView):
    ''' update a todo, then redirect back to its details page '''
    model = Todo
    fields = ['user', 'description', 'due_date']

    def get_success_url(self):
        return reverse('todo_details', kwargs={'pk': self.object.pk})

# Require login for this view
@method_decorator(login_required, name='dispatch')
class todo_delete(DeleteView):
    ''' Delete a specific todo (with confirmation page), and redirect back to list view '''
    model = Todo
    success_url = reverse_lazy('todo_list')
```

We'll also need to update our urls.py to link to these:
```python
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todos/$', views.todo_list.as_view(), name='todo_list'),
    url(r'^todo/create/$', views.todo_create.as_view(), name='todo_create'),
    url(r'^todo/(?P<pk>\d+)/$', views.todo_details.as_view(), name='todo_details'),
    url(r'^todo/(?P<pk>\d+)/update/$', views.todo_update.as_view(), name='todo_update'),
    url(r'^todo/(?P<pk>\d+)/delete/$', views.todo_delete.as_view(), name='todo_delete'),
]

```


## Templates

Finally,
we'll need to create the HTML template files that the views are looking for. Do to this, we'll need place the files in ```todos/templates/todos```

You may notice that the html snippits below mentions things like ```{% extends 'base.html' %} or {% block xxxx %}``` . These template-tags are part of Django's built in templating language. The ```extends``` tag allows us to do template inheritance... telling django to use base.html as the foundational template and allow us to add content to it.

Let's create this ```base.html```, which all the other snippets will leverage. For the purposes for the walk through we'll call our css/js libraries remotely, and keep the templating basic.


**todos/templates/base.html**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>To Do</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <!-- Bootstrap core CSS -->
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" media="screen" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">

        <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
        <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.2/html5shiv.js"></script>
        <script src="http://cdnjs.cloudflare.com/ajax/libs/respond.js/1.4.2/respond.js"></script>
        <![endif]-->
    </head>

    <body>

    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/">ToDos</a>
            </div>
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
                        {% if request.user.username %}
                            <a href="/accounts/logout/">Logout: {{ request.user.username }}</a>
                        {% else %}
                            <a href="/accounts/login/">Login</a>
                        {% endif %}
                    </li>
                    <li>
                        <a href="/accounts/register/">Register</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-12">
                    {% block body %}{% endblock %}
                </div>
            </div>
        </div> <!-- /container-fluid -->

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

    </body>
</html>


```


**todos/templates/todos/todo_list.html**
```html
{% extends 'base.html' %}

{% block body %}
<a href="{% url 'todo_create' %}">Create a new Todo</a>
<br><br>

{% if not object_list %}
<p>You don't have any todo's. Click the link above to make one</p>
{% else %}
<ul class="list-group">
    {%  for obj in object_list %}
    <li class="list-group-item">
        <a href="{% url 'todo_update' obj.id %}">
            <span class="glyphicon glyphicon-pencil" aria-hidden="true"></span>
        </a>
        &nbsp;
        <a href="{% url 'todo_delete' obj.id %}">
            <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>
        </a>
        &nbsp;
        <a href="{% url 'todo_details' obj.id %}">{{ obj.description }}</a>
        <span class="badge">{{ obj.due_date }}</span>
    </li>
    {% endfor %}
</ul>
{% endif %}

{% endblock %}
```

**todos/templates/todos/todo_update_form.html**
```html
{% extends 'base.html' %}

{% block body %}
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save" />
</form>
{% endblock %}
```

**todos/templates/todos/todo_form.html**
```html
{% extends 'base.html' %}

{% block body %}
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save" />
</form>
{% endblock %}
```

**todos/templates/todos/todo_detail.html**
```html
{% extends 'base.html' %}

{% block body %}
<a href="{% url 'todo_list' %}">Back to list</a><br><br>


Details <br>

ID: {{object.id}} <br>
Description - {{ object.description }} <br>
Due State - {{ object.due_date }}<br>

{% endblock %}

```

**todos/templates/todos/todo_confirm_delete.html**
```html
{% extends 'base.html' %}

{% block body %}
<form action="" method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    <input type="submit" value="Confirm" />
</form>
{% endblock %}
```



### Function based views

What if we need more than just CRUD-based views? 

Let's add a count of all Todos to our index view and page.


**views.py**
```python
def index(request):
    all_todos = Todo.objects.all()
    todo_count = all_todos.count()
    context = {
        'todo_count': todo_count, 
        'todos': all_todos
    }
    return render(request, "todos/index.html", context)
```

**todos/templates/todos/index.html**
```html
{% extends 'base.html' %}

{% block body %}

Todo Count: {{todo_count}}<br>
<a href="{% url 'todo_list' %}">List all todos</a>

{% endblock %}
```



## Django Admin
What if we need an administrative back-end where we can maintain our data, users, etc? Django built-in Admin app gives this all to us for free!

### Caveats
While the Admin app itself is great, you're limited to what the look and feel of the app is, as well as how far you can extend it. If you're running the limitation of admin, and fighting on the ways it wants you to do things, it's probably time to just abandon it and create your own app and write the logic/views/forms the way you need it.


### Adding Models into Admin
First, we need to create an admin user
``` python manage.py createsuperuser ```

**todos/admin.py**
```python
from django.contrib import admin

# Register your models here.
from .models import Todo

admin.site.register(Todo)

```

To test this, let's run our local test server
``` python manage runserver```

on your browser, go to http://localhost:8000/admin



### Further Reading

Intrigued? Want to learn more?
www.djangoproject.com


Django Plugins

django-extensions
django-modelutils
django-crispyforms

Make your stuff pretty
Bootstrap


