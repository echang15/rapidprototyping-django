from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



from todos.models import Todo
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the todo index.")



class todo_list(ListView):
	''' This will display a list of all the todos '''
	model = Todo

class todo_details(DetailView):
	''' This will display a page with the details of a single todo '''
	model = Todo


class todo_create(CreateView):
	''' This will display a simple form and allow users to create a todo '''
	model = Todo
	fields =['user','description','due_date']

	def get_success_url(self):
		return reverse('todo_details', kwargs={'pk' : self.object.pk})

class todo_update(UpdateView):
	''' update a todo, then redirect back to its details page '''
	model = Todo
	fields =['user','description','due_date']

	def get_success_url(self):
		return reverse('todo_details', kwargs={'pk' : self.object.pk})

class todo_delete(DeleteView):
	''' Delete a specific todo (with confirmation page), and redirect back to list view '''
	model = Todo
	success_url = reverse_lazy('todo_list')