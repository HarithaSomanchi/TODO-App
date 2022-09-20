from django.urls import path
from . import views
urlpatterns = [
path("books/",views.viewbooks.as_view()),
path("addbook/",views.Booksadd.as_view())

]