from django.urls import include, path

from ShelterHeroesServer.api.core.explore import views

app_name = "explore"

urlpatterns = [
    path("", views.ExploreViewSet.as_view()),
]
