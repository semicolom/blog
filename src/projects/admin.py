from django.contrib import admin

from main.admin import OrderedAdmin

from .models import Project


@admin.register(Project)
class ProjectAdmin(OrderedAdmin):
    fields = [
        'title',
        'description',
        'thumbnail',
        'photo',
        'color',
        'order',
        'is_active',
        'is_featured',
        'slug',
    ]
