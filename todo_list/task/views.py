# DRF imports
from rest_framework import viewsets
from rest_framework import permissions

# App imports
from todo_list.task.serializers import TaskSerializer, Task 


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filterset_fields = ['to_do', 'doing', 'done']

    def get_queryset(self):
        return Task.objects.all()