from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from blog import urls as blog_urls
from blog.views import PostListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^blog/', include(blog_urls, namespace='blog')),
]


# Django debug toolbar URLs
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
