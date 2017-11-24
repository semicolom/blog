from django.test import TestCase
from django.urls import reverse_lazy


class URLTestCase(TestCase):
    def test_home(self):
        self.assertEqual(reverse_lazy('home'), "/")
