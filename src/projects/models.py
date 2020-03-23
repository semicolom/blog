from django.db import models
from django.utils.text import slugify

from main.models import OrderedModel

from . import utils


class Category(models.Model):
    name = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        max_length=255,
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['order']

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Project(OrderedModel):
    thumbnail = models.ImageField(
        upload_to=utils.photo_upload_to,
        blank=True,
    )
    photo = models.ImageField(
        upload_to=utils.photo_upload_to,
        blank=True,
    )
    color = models.CharField(
        max_length=6,
        help_text='CSS RGB code'
    )
    categories = models.ManyToManyField(
        Category,
        related_name='projects',
        blank=True,
    )
    services = models.ManyToManyField(
        'services.Service',
        related_name='projects',
        blank=True,
    )

    def get_categories(self):
        return ' '.join(self.categories.values_list('slug', flat=True))
