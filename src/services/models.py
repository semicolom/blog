from django.db import models

from main.models import OrderedModel

from . import utils


class Service(OrderedModel):
    short_description = models.TextField()
    photo = models.ImageField(
        upload_to=utils.photo_upload_to,
        blank=True,
    )
    icon = models.CharField(
        max_length=255,
        blank=True,
        help_text='Font Awesome icon ID. https://fontawesome.com/icons'
    )
