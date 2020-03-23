from django.contrib import admin

from main.admin import OrderedAdmin

from .models import Project, Category


@admin.register(Category)
class ProjectCategoryAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]


@admin.register(Project)
class ProjectAdmin(OrderedAdmin):
    fields = [
        'title',
        'description',
        'thumbnail',
        'photo',
        'color',
        'categories',
        'services',
        'order',
        'is_active',
        'is_featured',
        'slug',
    ]

    filter_horizontal = [
        'categories',
        'services',
    ]
