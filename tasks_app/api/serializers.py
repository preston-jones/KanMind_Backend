from rest_framework import serializers
from tasks_app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model
    """
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at', 'user']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']


class TaskCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new tasks
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Task.objects.create(**validated_data)