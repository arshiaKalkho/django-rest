from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response):
    return HttpResponse("<h1>worked</h1>")

def getID(response, id):
    list = ToDoList.objects.get(id=id)
    item = list.item_set.get(id=1)
    return HttpResponse("<h1> %s </h1> <br/> <p> %s </p>" % (list.name, str(item.text)) )
