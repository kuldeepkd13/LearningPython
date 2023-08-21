
from django.urls import path
from tdd import views

urlpatterns = [
 path("view/<str:id>/" , views.view  , name="view"),
 path("create" , views.create  , name="create"),
 path("delete" , views.delete  , name="delete")
]