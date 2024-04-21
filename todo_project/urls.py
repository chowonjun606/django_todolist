# todo_project/urls.py 파일 수정

from django.urls import include, path

urlpatterns = [
    path('', include('todos.urls')),  # 'todos' 애플리케이션의 urls.py를 참조
]
