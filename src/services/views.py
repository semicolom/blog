from django.views.generic import ListView

from .models import Service


class ServiceListView(ListView):
    model = Service
