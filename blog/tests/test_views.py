from django.test import TestCase
from django.urls import reverse_lazy

from model_mommy import mommy

from ..models import Post


class PostListViewTestCase(TestCase):
    url = reverse_lazy('home')

    def test_context(self):
        mommy.make(Post)

        response = self.client.get(self.url)
        self.assertListEqual(
            list(response.context_data.get('post_list')),
            list(Post.objects.all())
        )
