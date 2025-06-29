from rest_framework.generics import ListCreateAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from .serializers import TaskSerializer
from ...models import Task


class TaskListApiView(ListCreateAPIView,IsAdminUser):
    permission_classes = [IsAdminUser]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()