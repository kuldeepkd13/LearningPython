from django.urls import path
from . import views

urlpatterns = [
    path('<str:city>/', views.weather_view, name='weather'),
    path('', views.weather_create_view, name='create_weather'),
    path('<str:city>/update/', views.weather_update_view, name='update_weather'),
    path('<str:city>/delete/', views.weather_delete_view, name='delete_weather'),
]
