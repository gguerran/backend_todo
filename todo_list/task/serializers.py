from rest_framework import serializers
from todo_list.task.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Task
        ordering = ['created_at']
        fields = ['id', 'title', 'author', 'description', 'to_do',
            'doing', 'done', 'created_at', 'modified_at']
        extra_kwargs = {
            'id': {'read_only': True}, 'created_at': {'read_only': True},
            'modified_at': {'read_only': True},
        }
