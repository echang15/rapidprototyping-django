from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.todo_create.as_view(), name='create'),
    #url(r'^(?P<id>+)/$', views.detail, name='detail'),
    #url(r'^(?P<id>+)/update/$', views.update, name='update'),
    #url(r'^(?P<id>+)/delete/$', views.delete, name='delete'),
]