from django.test import TestCase

from ..models import Post


class PostTestCase(TestCase):
    def _create_post(self):
        self.post = Post.objects.create(
            title="Test",
            subtitle="Test test",
            body="Test Test test"
        )

    def test_fields(self):
        self._create_post()

        self.assertEqual(self.post.title, "Test")
        self.assertEqual(self.post.subtitle, "Test test")
        self.assertEqual(self.post.body, "Test Test test")
        self.assertEqual(self.post.slug, "test")

    def test_str(self):
        self._create_post()

        self.assertEqual(str(self.post), "Test")

    def test_get_last_post(self):
        self.assertIsNone(Post.get_last_post())
        self._create_post()
        self.assertEqual(self.post.title, "Test")
