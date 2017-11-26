from django.db import models

from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = RichTextField()
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return '{}'.format(self.title)
