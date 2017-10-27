# Rapid Prototyping with Django (tl;dr)

Looking for a more complete walkthrough? [Look here](README.md)

## Getting started

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp todos
```

**myproject/settings.py**

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

Add the following lines of code to the bottom of the ```settings.py``` file.

```python
# Login redirection settings
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

# Security Settings
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

**todos/models.py**

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

```bash
python manage.py makemigrations todos
python manage.py migrate
python manage.py createsuperuser
```

**todos/admin.py**

```python
from django.contrib import admin

# Register your models here.
from .models import Todo

admin.site.register(Todo)

```


```bash
python manage.py runserver
open htpp://127.0.0.1:8000
```

**todos/urls.py**

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todos/$', views.todo_list.as_view(), name='todo_list'),
    url(r'^todo/create/$', views.todo_create.as_view(), name='todo_create')
]
```

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

**todos/views.py**

```python
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count

from django.contrib.auth.models import User
from todos.models import Todo


def index(request):
    todos_by_user = User.objects.annotate(num_todos=Count('todo'))
    context = {
        'todos_by_user': todos_by_user
    }
    return render(request, "todos/index.html", context)


class todo_list(ListView):
    ''' This will display a list of all the todos '''
    model = Todo


@method_decorator(login_required, name='dispatch')  # Require login
class todo_create(CreateView):
    ''' This will display a simple form and allow users to create a todo '''
    model = Todo
    fields = ['user', 'description', 'due_date']

    def get_success_url(self):
        return reverse('todo_list')

```


```bash
mkdir -p todos/templates/todos/
mkdir -p todos/templates/registration/
```

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
                    <a class="navbar-brand" href="/">Home</a>
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

**todos/templates/registration/login.html**

```html
{% extends 'base.html' %}

{% block body %}
<form action="" method="post">{% csrf_token %}
{{form}}
<input type="submit" value="Confirm" />
</form>
{% endblock %}
```

**todos/templates/registration/register.html**

```html
{% extends 'base.html' %}

{% block body %}
<form action="" method="post">{% csrf_token %}
{{form}}
<input type="submit" value="Confirm" />
</form>
{% endblock %}
```

**todos/templates/todos/index.html**

```html
{% extends 'base.html' %}

{% block body %}

Todo Count by User:<br>
<ul class="list-group">
    {%  for obj in todos_by_user %}
    <li class="list-group-item">
        {{ obj.username }}
        <span class="badge">{{ obj.num_todos }}</span>
    </li>
    {% endfor %}
</ul>
<a href="{% url 'todo_list' %}">List all todos</a>

{% endblock %}
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
        {{ obj.description }}
        <span class="badge">{{ obj.due_date }}</span>
    </li>
    {% endfor %}
</ul>
{% endif %}

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
