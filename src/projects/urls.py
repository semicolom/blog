from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path(
        route='',
        view=views.ProjectListView.as_view(),
        name='list',
    ),
    path(
        route='category/<slug:slug>/',
        view=views.ProjectCategoryDetailView.as_view(),
        name='category-detail',
    ),
    path(
        route='<slug:slug>/',
        view=views.ProjectDetailView.as_view(),
        name='detail',
    ),
]
