from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('list_task/', views.TaskListApiView.as_view(), name='task-list_api'),
    path("list_task/<int:pk>/", views.TaskDetailApiView.as_view(), name='task-detail_api'),
]