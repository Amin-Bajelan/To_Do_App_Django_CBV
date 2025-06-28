from django.urls import path
from . import views
urlpatterns = [
    path('list_task/', views.ListTasks.as_view(), name='task_list'),
    path('delete_task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
    path('toggle_task/<int:id>', views.ToggleTaskView.as_view(), name='toggle_task'),
    path('tak/<int:pk>/edit/',views.UpdateTaskView.as_view(), name='edit_task'),
    path('task/add/', views.AddTask.as_view(), name='add_task'),

]