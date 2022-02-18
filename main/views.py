from sqlite3 import complete_statement
from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

def index(response, id):
    list = ToDoList.objects.get(id=id)
    
    if response.method == "POST":
        #print("received:    ",response.POST)
        if response.POST.get('save'):#update new item if are completed or not 
            for item in list.item_set.all():
                if response.POST.get('c' + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get('newItem'):
            txt = response.POST.get('new')
            print("text: ",txt)
            if len(txt) > 2: #minlength of two
                list.item_set.create(text=txt, complete=False)
                
            else:
                print('inavlid input')
        
        
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
    
    
