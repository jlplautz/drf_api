from vmtodo.drf.models import Tasks
from vmtodo.drf.serializers import TaskSerializer
from rest_framework import generics


class TaskList(generics.ListCreateAPIView):
    # esta classe vai fazer o GET e POST
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    # para fazer o GET com ID / Update e DELETE
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer



