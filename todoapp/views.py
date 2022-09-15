from django.shortcuts import render
from .models import TodoListItem 
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def todoappView(request):
    instance = request.user
    print(instance)
    all_todo_items = TodoListItem.objects.filter(author = instance ).values()
    
    if len(all_todo_items)>0:
        return render(request, 'view.html',
                 {'all_items':all_todo_items,
                  'author': instance})
    else:
        msg="No Data Available"
        return render(request,"d.html",{'msg':msg})
    
    
def index(request):
    return render(request,'welcome.html')

def addTodoView(request):
    x = request.POST['content']
    y= request.POST['rating']
    z=request.POST['value']
    
    if TodoListItem.objects.filter(value =z).exists():
        msg="No, The data with that id is already available"
        return render(request,"d.html",{'msg':msg})
       
    else:
        new_item = TodoListItem(content = x , rating = y, value=z)
        new_item.author=request.user
        new_item.save()
    #return HttpResponseRedirect('todoapp') 
    return render(request,"redirect.html")

def deleteTodoView(request):
    i=request.POST['value']
    
    if TodoListItem.objects.filter(value =i).exists():
        y = TodoListItem.objects.get(value= i)
        y.delete()
    else:
        msg="No The data with that id is not available"
        return render(request,"d.html",{'msg':msg})
        
    #return HttpResponseRedirect("") 
    return render(request,"redirect.html")
def insertion(request):
    return render(request,'insertion.html')
def delete(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request,"todo.html", {'all_items':all_todo_items})
def home(request):
    return render(request,"home.html")
