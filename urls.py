from django.conf.urls import url
from django.contrib import admin

from blog.views import EntryListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', EntryListView.as_view(), name='home'),
]
