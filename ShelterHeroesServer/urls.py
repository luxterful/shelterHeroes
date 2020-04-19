from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("", RedirectView.as_view(url="/admin/")),
    path("admin/", admin.site.urls),
    path("api/", include("ShelterHeroesServer.api.urls", namespace="api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
