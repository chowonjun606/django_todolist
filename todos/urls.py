# todos/urls.py 파일

from django.urls import path
from .views import todo_list, add_todo, complete_todo

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('add/', add_todo, name='add_todo'),
    path('complete/<int:pk>/', complete_todo, name='complete_todo'),
]
