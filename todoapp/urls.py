from django.urls import path
from . import views
urlpatterns = [
     path("todoapp/",views.index, name="todoapp"),
     path("",views.index),
     path("insertion/",views.insertion),
     path("delete/",views.delete),
    path("viewdata/",views.todoappView),
    path("addTodoItem/",views.addTodoView),
    path("home/",views.home),
    path('deleteTodoItem/', views.deleteTodoView)
]