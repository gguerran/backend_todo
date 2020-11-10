# Importações DRF
from rest_framework import routers
from django.urls import re_path, include

from todo_list.task import views

# nome da app
app_name = 'task'

router = routers.DefaultRouter()

router.register(
    'task', views.TaskViewSet, basename='task'
)

urlpatterns = [
    re_path('^', include(router.urls)),
]