from django.contrib import admin
from .models import Task

# Register your models here.

class AdminTask(admin.ModelAdmin):
    model = Task
    list_display = ['owner', 'title', 'created_at']
    search_fields = ['owner', 'title', 'created_at']


admin.site.register(Task,AdminTask)