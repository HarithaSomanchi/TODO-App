from enum import unique
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField() 
    rating = models.IntegerField(null=True)
    value= models.IntegerField(default=0, unique=True)
    author=models.ForeignKey(User,default=None, on_delete=models.CASCADE)
    
    def __str__(self):
         return f"{self.content},{self.rating}"
     
class Books(models.Model):
    title = models.TextField()
    pages = models.IntegerField()
    
    def __str__(self):
        return f"{self.title}"

    
    

