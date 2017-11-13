from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class Entry(TimeStampedModel, TitleSlugDescriptionModel):
    def __str__(self):
        return '{}'.format(self.title)
