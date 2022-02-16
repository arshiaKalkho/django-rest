from unicodedata import name
from django.db import models

# manage.py makemigrations <name of app in this case "main"> on change so django "commits" you changes to project
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    ToDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text