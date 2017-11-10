from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class Entry(TimeStampedModel, TitleSlugDescriptionModel):
    pass
