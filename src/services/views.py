from django.views.generic import ListView, DetailView

from .models import Service


class ServiceListView(ListView):
    queryset = Service.active.all()


class ServiceDetailView(DetailView):
    queryset = Service.active.all()

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'projects': self.object.projects.all(),
            'other_services': self.queryset.exclude(id=self.object.id),
        }
