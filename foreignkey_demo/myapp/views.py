
from django.shortcuts import render,redirect
from .models import *
from django.http import *
from .forms import *


# Create your views here.
def index(request):
    records = Book.objects.all()
    # for i in records:
    #     print(i.title)
    #     print(i.books_author.name)

    # return HttpResponse('ok')
    return render(request,'home.html',{'rec':records})


def create_author(request):
    if request.method =='POST':
        form=author_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form =author_form()

    return render(request,'author.html',{'form':form})

def create_book(request):
    if request.method =='POST':
        form=books_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =books_form()

    return render(request,'book.html',{'form':form})
