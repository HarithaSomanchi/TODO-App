from django import forms
from todoapp.models import Books


class Bookform(forms.ModelForm):
    class Meta:
        model=Books
        fields = ["title" ,"pages"]