from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from tasks_app.models import Task
from .serializers import TaskSerializer, TaskCreateSerializer
from .permissions import IsTaskOwner


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task model
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsTaskOwner]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        return TaskSerializer

    @action(detail=True, methods=['post'])
    def toggle_completed(self, request, pk=None):
        """
        Toggle task completion status
        """
        task = self.get_object()
        task.completed = not task.completed
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)