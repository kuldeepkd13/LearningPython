from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.pdf_upload_view, name='pdf_upload'),
    path('question/', views.question_view, name='question_view'),
]
