from django.db import models

from main.models import OrderedModel

from . import utils


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
