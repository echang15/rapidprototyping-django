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
