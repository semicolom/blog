from django.urls import path, re_path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    re_path('(?P<slug>[\w-]+)/', views.PostDetailView.as_view(), name='detail'),
]
