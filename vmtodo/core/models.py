from django.db import models
from django import forms


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    disable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ('-created_at',)

    def __str__(self):
        return self.task


class TaskForm(forms.ModelForm):
    class Meta:
        model =Tasks
        fields = 'task disable'.split()
