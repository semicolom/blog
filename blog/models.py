from django.db import models

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    body = models.TextField()
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return '{}'.format(self.title)
