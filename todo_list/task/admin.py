from django.contrib import admin
from todo_list.task.models import Task


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'to_do',
     'doing', 'done', 'created_at']
    ordering = ['created_at',]

    fieldsets = [
        [None, {'fields': ['title', 'description', 'to_do',
     'doing', 'done']}],
    ]


admin.site.register(Task, TaskModelAdmin)