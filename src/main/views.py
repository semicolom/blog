from django.views.generic.base import TemplateView

from blog.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update(dict(
            last_post=Post.objects.all()[0]
        ))
        return context
