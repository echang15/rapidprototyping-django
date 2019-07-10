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
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description
```

```bash
python manage.py makemigrations todos
python manage.py migrate
```

**todos/admin.py**

```python
from django.contrib import admin

# Register your models here.
from .models import Todo

admin.site.register(Todo)
```


```bash
python manage.py createsuperuser
python manage.py runserver
open htpp://127.0.0.1:8000
```

**todos/urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todo_list.as_view(), name='todo_list'),
    path('todo/create/', views.todo_create.as_view(), name='todo_create')
]
```

**myproject/urls.py**

```python
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name="user_login"),
    path('accounts/logout/', LogoutView.as_view(), name="user_logout"),
    path('accounts/register/', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/'
    )),
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
]
```

**todos/views.py**

```python
from django.shortcuts import render
from django.urls import reverse
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
mkdir -p todos/templates/todos
touch todos/templates/base.html
touch todos/templates/registration/login.html
touch todos/templates/registration/register.html
touch todos/templates/todos/index.html
touch todos/templates/todos/todo_list.html
touch todos/templates/todos/todo_form.html
```

**todos/templates/base.html**

```html
<!DOCTYPE html>
<html>

<head>
    <title>ToDo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css"
        integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
</head>

<body>

    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
        <a class="navbar-brand" href="/">Todo <i class="fas fa-clipboard-list"></i></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="">
            <ul class="navbar-nav mr-auto"></ul>
            <span class="navbar-text">
                {% if request.user.username %}
                <a href="/accounts/logout/">Logout</a>
                {% else %}
                <a href="/accounts/login/">Login</a> / 
                <a href="/accounts/register/">Register</a>
                {% endif %}
            </span>
            
        </div>
    </nav>
    <br>
    <main role="main" class="container-fluid">
        <div class="row">
            <div class="col-sm-12">
                {% block body %}{% endblock %}
            </div>
        </div>
    </main> <!-- /container -->

    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
    </script>

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

<h3>Todo count by user:</h3>
<ul class="list-group">
    {%  for obj in todos_by_user %}
    <li class="list-group-item d-flex justify-content-between align-items-center">
        {{ obj.username }}
        <span class="badge badge-primary badge-pill">{{ obj.num_todos }}</span>
    </li>
    {% endfor %}
</ul>
<br>
<a class="btn btn-primary" href="{% url 'todo_list' %}">List all Todos</a>

{% endblock %}
```

**todos/templates/todos/todo_list.html**

```html
{% extends 'base.html' %}

{% block body %}

{% if not object_list %}
<p>You don't have any todo's. Click the link above to make one</p>
{% else %}
<form class="form-inline">
    <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
    <button class="btn btn-secondary my-sm-0" type="submit">Search</button>
</form>
<br>
<div class="table-responsive">
    <table class="table table-hover">
        <thead class="thead-dark">
            <tr>
                <th scope="col">For</th>
                <th scope="col">Description</th>
                <th scope="col">Due</th>
            </tr>
        </thead>
        <tbody>
            {%  for obj in object_list %}
            <tr>
                <th scope="row">{{ obj.user.username }}</th>
                <td>{{ obj.description }}</td>
                <td>{{ obj.due_date }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endif %}
<br>
<a class="btn btn-primary" href="{% url 'todo_create' %}">New Todo</a>
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
