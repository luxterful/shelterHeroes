from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("auth/", include("ShelterHeroesServer.api.auth.urls", namespace="auth")),
    path("core/", include("ShelterHeroesServer.api.core.urls", namespace="core")),
]
