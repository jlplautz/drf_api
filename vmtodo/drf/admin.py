from django.contrib import admin
from vmtodo.drf.models import Tasks

@admin.register(Tasks)
class Admindrf(admin.ModelAdmin):
    list_display = ('id', 'task', 'created_at', 'disable')
