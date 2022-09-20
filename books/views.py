from django.shortcuts import render
from .forms import Bookform
from django.views import View
from django.views.generic.base import TemplateView
from todoapp.models import Books
# Create your views here.

class Booksadd(View):
    def get(self,request):
        form = Bookform()
        return render(request , "Booksform.html" ,{"form":form})
    def post(self,request):
        form=Bookform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"redirect.html")
        else:
            return render(request , "Booksform.html" ,{"form":form})
class viewbooks(TemplateView):
    template_name = "viewbook.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        data=Books.objects.all()
        context['data']= data
        return context
    def get_queryset(self):
        return super().get_queryset()
    
    
    

            