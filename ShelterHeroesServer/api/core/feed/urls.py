from django.urls import include, path

from ShelterHeroesServer.api.core.feed import views

app_name = "feed"

urlpatterns = [
    path("", views.FeedViewSet.as_view()),
]
