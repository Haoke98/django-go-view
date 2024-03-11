from django.contrib import admin
from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'state', 'createTime', 'updateTime', 'createUserId', 'deletedTime', 'cover',
                    'remarks']
    list_filter = ['state', 'createUserId']
    date_hierarchy = 'createTime'
