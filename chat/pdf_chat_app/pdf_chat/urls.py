from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdf_upload_view, name='upload'),
    path('chat/', views.chat_view, name='chat'),
    path('end_chat/', views.end_chat_view, name='end_chat'),  
]
