from rest_framework import serializers

from .models import Task, List


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('user_list',)


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(Task, many=True)

    class Meta:
        model = List
        fields = ('id', 'name', 'tasks')
