from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from blog import views as blog_views

urlpatterns = [
    path('{}/'.format(settings.ADMIN_URL), admin.site.urls),
    path('', blog_views.PostListView.as_view(), name='home'),
    # path('', views.HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
]


# Django debug toolbar URLs
if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
