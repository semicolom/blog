from django.views.generic import ListView, DetailView

from .models import Project


class ProjectListView(ListView):
    queryset = Project.active.all()


class ProjectDetailView(DetailView):
    queryset = Project.active.all()

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'without_header_img': True,
            'other_projects': self.queryset.exclude(id=self.object.id),
        }
