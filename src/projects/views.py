from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Project, Category


class ProjectListView(ListView):
    queryset = Project.active.all()
    category = None

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'categories': Category.objects.all(),
            'category': self.category,
        }


class ProjectDetailView(DetailView):
    queryset = Project.active.all()

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'without_header_img': True,
            'services': self.object.services.active.all(),
            'other_projects': self.queryset.filter(
                categories__in=self.object.categories.all(),
            ).exclude(
                id=self.object.id,
            ),
        }


class ProjectCategoryDetailView(ProjectListView):
    def dispatch(self, request, *args, **kwargs):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs['slug'],
        )
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.filter(categories=self.category)
