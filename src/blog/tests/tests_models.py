from django.test import TestCase

from ..models import Post


class PostTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test",
            subtitle="Test test",
            body="Test Test test"
        )

    def test_fields(self):
        self.assertEqual(self.post.title, "Test")
        self.assertEqual(self.post.subtitle, "Test test")
        self.assertEqual(self.post.body, "Test Test test")
        self.assertEqual(self.post.slug, "test")

    def test_str(self):
        self.assertEqual(str(self.post), "Test")
