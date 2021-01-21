from django.contrib import admin
from vmtodo.core.models import Tasks


@admin.register(Tasks)
class AdminCore(admin.ModelAdmin):
    list_display = ('id', 'task', 'created_at', 'disable')
