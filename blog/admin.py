from django.contrib import admin

from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'modified'
    )

    list_filter = [
        'created'
    ]

    search_fields = [
        'title',
        'description'
    ]
