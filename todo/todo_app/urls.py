from django.urls import path
from . import views

urlpatterns = [
    path('todo-list/', views.todoList, name="todo-list"),
    path('todo-create', views.todoCreate, name="todo-create"),
    path('todo-delete/<str:pk>', views.todoDelete, name="todo-delete"),
    path('todo-completed-update/<str:pk>', views.todoComletedUpdate,
         name="todo-completed-update"),
]
