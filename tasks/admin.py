from django.contrib import admin
from .models import Task


# Register your models here.
class Tasks_admin(admin.ModelAdmin):
    readonly_fields=("created", )
admin.site.register(Task, Tasks_admin)
