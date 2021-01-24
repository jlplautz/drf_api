from django.db import models


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    disable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ('-created_at',)



