from django import forms
from .models import *


class author_form(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class books_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'