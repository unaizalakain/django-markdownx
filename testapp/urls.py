from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from testapp.views import TestFormView


urlpatterns = [
    url(r'^$', TestFormView.as_view(), name='form_view'),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
