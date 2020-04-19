from django.urls import include, path

app_name = "core"

urlpatterns = [
    path(
        "shelters/",
        include("ShelterHeroesServer.api.core.shelters.urls", namespace="shelters"),
    ),
    path(
        "animals/",
        include("ShelterHeroesServer.api.core.animals.urls", namespace="animals"),
    ),
    path(
        "posts/", include("ShelterHeroesServer.api.core.posts.urls", namespace="posts")
    ),
    path("feed", include("ShelterHeroesServer.api.core.feed.urls", namespace="feed")),
]
