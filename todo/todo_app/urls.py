from django.urls import path
from . import views

urlpatterns = [
    path('todo-list/', views.todoList),
    path('todo-upadate/<str:pk>', views.todoListUpdate),
]
