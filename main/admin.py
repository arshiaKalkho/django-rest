from django.contrib import admin
from .models import ToDoList, Item

#give django admin access to the ToDoList database object
#so its accessible from the admin dashboard
admin.site.register(ToDoList)
admin.site.register(Item)

