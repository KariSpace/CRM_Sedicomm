

from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('', views.todo, name='todo'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]