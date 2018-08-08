from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from blog import views as blog_views


urlpatterns = [
    path('{}'.format(settings.ADMIN_URL), admin.site.urls),
    path('', blog_views.PostListView.as_view(), name='home'),
    # path('', views.HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
]

# On development serve media and static files using django
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Django debug toolbar URLs
if settings.DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
