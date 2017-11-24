from django.test import TestCase
from django.urls import reverse_lazy

from model_mommy import mommy

from ..models import Post


class URLTestCase(TestCase):
    def test_detail(self):
        post = mommy.make(Post, title='Test')

        self.assertEqual(
            reverse_lazy('blog:detail', kwargs=dict(slug=post.slug)),
            "/blog/test/"
        )
