from django.views.generic.base import TemplateView

from djtools.blog.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['last_post'] = Post.get_last_post()

        return context
