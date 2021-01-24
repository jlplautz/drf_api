from rest_framework import serializers
from vmtodo.drf.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Qual o modelo e quais os campos
        model = Tasks
        fields = ('id', 'task', 'disable', 'created_at')
