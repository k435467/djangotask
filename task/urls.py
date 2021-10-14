from django.urls import path
from task import views

urlpatterns = [
    path('tasks', views.task_list, name='tasks'),
    path('task', views.task_create, name='task-create'),
    path('task/<int:pk>', views.task_detail, name='task'),
]