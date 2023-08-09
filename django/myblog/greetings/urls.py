from django.contrib import admin
from django.urls import path
from greetings import views

urlpatterns = [
    path("", views.index, name="home"),
    path("greet/<str:username>", views.greet, name="greet"),
    path("farewell/<>str:username",views.farewell,name="farewell")
]

  