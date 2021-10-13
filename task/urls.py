from django.urls import path
from task import views

urlpatterns = [
    path('tasks', views.task_list),
    path('task', views.task_create),
    path('task/<int:pk>', views.task_detail),
]