from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.getID, name="getID"),
    #path("", views.index, name="index"),
]