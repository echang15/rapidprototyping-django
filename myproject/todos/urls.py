from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todos/$', views.todo_list.as_view(), name='todo_list'),
    url(r'^todo/create/$', views.todo_create.as_view(), name='todo_create'),
    url(r'^todo/(?P<pk>\d+)/$', views.todo_details.as_view(), name='todo_details'),
    url(r'^todo/(?P<pk>\d+)/update/$', views.todo_update.as_view(), name='todo_update'),
    url(r'^todo/(?P<pk>\d+)/delete/$', views.todo_delete.as_view(), name='todo_delete'),
]
