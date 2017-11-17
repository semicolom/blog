from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from blog.views import PostListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name='home'),
]


# Django debug toolbar URLs
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
