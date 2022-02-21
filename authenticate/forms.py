from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class registerForm(UserCreationForm):#modify forms to have custom fields like email
    email = forms.EmailField()
    
    class Meta:#change parent data fields
        model = User
        fields = ["username", "email", "password1", "password2", ] 
