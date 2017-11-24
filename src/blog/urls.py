from django.conf.urls import url

from .views import PostDetailView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'),
]
