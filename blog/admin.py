from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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
        'subtitle',
        'body'
    ]
