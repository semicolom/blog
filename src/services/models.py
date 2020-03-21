from django.db import models
from django.utils.text import slugify

from . import utils, managers


class Service(models.Model):
    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        max_length=255,
    )
    short_description = models.TextField()
    description = models.TextField(
        blank=True,
    )
    photo = models.ImageField(
        upload_to=utils.photo_upload_to,
        blank=True,
    )
    icon = models.CharField(
        max_length=255,
        blank=True,
        help_text='Font Awesome icon ID. https://fontawesome.com/icons'
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
        ordering = ['order']
        index_together = [
            ['is_active', 'order'],  # Service list
            ['is_active', 'is_featured', 'order'],  # Featured on home
        ]

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def has_content(self) -> bool:
        return bool(self.description and self.photo)
