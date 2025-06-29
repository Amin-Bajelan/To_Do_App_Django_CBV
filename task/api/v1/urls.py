from django.urls import path
from . import views

urlpatterns = [
    path('list_task/', views.TaskListApiView.as_view(), name='task-list'),

]