from django.contrib import admin

# Register your models here.
from .models import TodoListItem,Books

admin.site.register(TodoListItem)
admin.site.register(Books)