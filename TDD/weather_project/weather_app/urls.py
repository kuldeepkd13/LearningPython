from django.urls import path
from weather_app import views

urlpatterns = [
    path('weather/<str:city>/', views.weather_view, name='weather'),
]