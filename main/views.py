from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id):
    list = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {"name":list.name})

def home(response):
    return render(response, "main/home.html", {"name": 'no value set'})
    
