from django.views.generic.base import TemplateView

from djtools.blog.models import Post
from services.models import Service


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return {
            'last_post': Post.get_last_post(),
            'featured_services': Service.featured.all(),
            **super().get_context_data(**kwargs)
        }
