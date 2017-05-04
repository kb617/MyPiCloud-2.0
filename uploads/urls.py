from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
#    url(r'^simple/$', views.simple_upload, name='simple_upload'),
    url(r'^form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^delete/documents/(?P<doc_id>[0-9]+)/$', views.delete_document, name='delete_document'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
