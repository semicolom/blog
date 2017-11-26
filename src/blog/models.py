from django.db import models

from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    subtitle = models.CharField(max_length=255)
    body = RichTextField()
    image = models.ImageField(upload_to='posts')

    def __str__(self):
        return '{}'.format(self.title)

    @classmethod
    def get_last_post(cls):
        try:
            last_post = Post.objects.all()[0]
        except IndexError:
            last_post = None

        return last_post
