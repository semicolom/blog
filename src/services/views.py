from django.views.generic import ListView, DetailView

from .models import Service


class ServiceListView(ListView):
    queryset = Service.active.all()


class ServiceDetailView(DetailView):
    queryset = Service.active.all()
