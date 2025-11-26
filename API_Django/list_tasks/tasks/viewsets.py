from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Tasks

class TasksViewSet(viewsets.ModelViewSet):
    serializer_class= TaskSerializer
    queryset= Tasks.objects.all()

    