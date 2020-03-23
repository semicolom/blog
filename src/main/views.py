from django.views.generic.base import TemplateView

from djtools.blog.models import Post
from projects.models import Project
from services.models import Service


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return {
            'last_post': Post.get_last_post(),
            'featured_services': Service.featured.all()[:3],
            'featured_projects': Project.featured.all()[:3],
            **super().get_context_data(**kwargs)
        }
