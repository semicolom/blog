from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from blog import urls as blog_urls

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^blog/', include(blog_urls, namespace='blog')),
]


# Django debug toolbar URLs
if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
