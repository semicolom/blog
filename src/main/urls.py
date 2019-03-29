from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from djtools.contact.views import ContactRequestView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('{}/'.format(settings.ADMIN_URL), admin.site.urls),
    path('blog/', include('djtools.blog.urls')),
    path('work-with-me/', ContactRequestView.as_view(), name='contact'),
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
