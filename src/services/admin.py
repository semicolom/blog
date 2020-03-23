from django.contrib import admin

from main.admin import OrderedAdmin

from .models import Service


@admin.register(Service)
class ServiceAdmin(OrderedAdmin):
    fields = [
        'title',
        'short_description',
        'description',
        'icon',
        'photo',
        'order',
        'is_active',
        'is_featured',
        'slug',
    ]
