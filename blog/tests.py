from django.test import TestCase

from .models import Entry


class EntryTestCase(TestCase):
    def test_fields(self):
        entry = Entry.objects.create(
            title="Test",
            description="Test test"
        )
        self.assertEqual(entry.title, "Test")
        self.assertEqual(entry.description, "Test test")
        self.assertEqual(entry.slug, "test")
