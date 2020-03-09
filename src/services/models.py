from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='services')
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    # TODO: Order by ordering
    # TODO: Default manager return active ones

    def __str__(self):
        return f"{self.name}"
