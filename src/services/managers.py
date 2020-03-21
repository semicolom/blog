from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class FeaturedManager(ActiveManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_featured=True)
