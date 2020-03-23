from django.db import models
from django.utils.text import slugify

from . import managers


class OrderedModel(models.Model):
    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        max_length=255,
    )
    description = models.TextField(
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
    )
    is_active = models.BooleanField(
        default=True,
        db_index=True,
    )
    is_featured = models.BooleanField(
        default=False,
        db_index=True,
    )

    objects = models.Manager()
    active = managers.ActiveManager()
    featured = managers.FeaturedManager()

    class Meta:
        abstract = True
        ordering = ['order']
        index_together = [
            ['is_active', 'order'],  # Service list
            ['is_active', 'is_featured', 'order'],  # Featured on home
        ]

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
