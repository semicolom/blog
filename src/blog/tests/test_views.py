from django.test import TestCase
from django.urls import reverse_lazy

from model_mommy import mommy

from ..models import Post


class PostListViewTestCase(TestCase):
    url = reverse_lazy('home')

    def test_list_order(self):
        post_1 = mommy.make(Post, body='Test')
        post_2 = mommy.make(Post, body='Test')

        response = self.client.get(self.url)
        self.assertListEqual(
            list(response.context_data.get('post_list')),
            [post_2, post_1]
        )
