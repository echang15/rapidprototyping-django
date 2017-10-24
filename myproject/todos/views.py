from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from todos.models import Todo
# Create your views here.


def index(request):
    todo_count = Todo.objects.all().count()
    return render(request, "todos/index.html",{'todo_count': todo_count})


class todo_list(ListView):
    ''' This will display a list of all the todos '''
    model = Todo


class todo_details(DetailView):
    ''' This will display a page with the details of a single todo '''
    model = Todo


@method_decorator(login_required, name='dispatch')
class todo_create(CreateView):
    ''' This will display a simple form and allow users to create a todo '''
    model = Todo
    fields = ['user', 'description', 'due_date']

    def get_success_url(self):
        return reverse('todo_details', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class todo_update(UpdateView):
    ''' update a todo, then redirect back to its details page '''
    model = Todo
    fields = ['user', 'description', 'due_date']

    def get_success_url(self):
        return reverse('todo_details', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class todo_delete(DeleteView):
    ''' Delete a specific todo (with confirmation page), and redirect back to list view '''
    model = Todo
    success_url = reverse_lazy('todo_list')
