from django.contrib import admin


class OrderedAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
        'is_featured',
        'order',
    ]

    list_filter = [
        'is_active',
        'is_featured',
    ]

    readonly_fields = [
        'slug',
    ]
