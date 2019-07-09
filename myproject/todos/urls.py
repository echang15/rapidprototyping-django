from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todo_list.as_view(), name='todo_list'),
    path('todo/create/', views.todo_create.as_view(), name='todo_create')
]
