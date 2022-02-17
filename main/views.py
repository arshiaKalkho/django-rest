from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

def index(response, id):
    list = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"list":list})

def home(response):
    return render(response, "main/home.html",{})
    
def create(response):#create new todolist 
    if response.method == "POST":#if user is submitting 
        form = CreateNewList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            todolist = ToDoList(name=name)
            todolist.save()
            return HttpResponseRedirect("/%i" %todolist.id)   
    else:#if user wants the empty form itself to fill
        form = CreateNewList()
    
    return render(response, "main/create.html",{"form": form})
    
    
