from django.shortcuts import render, redirect
from .forms import registerForm

def register(response):

    if response.method == "POST":
        form = registerForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = registerForm()

    return render(response, 'authenticate/register.html',{'form':form})

def login(response):
    form = registerForm()
    return render(response, 'authenticate/login.html',{'form':form})