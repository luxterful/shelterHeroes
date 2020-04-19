from django.urls import include, path

from ShelterHeroesServer.api.core.animals import views

app_name = "animals"

urlpatterns = [
    path("", views.AnimalListViewSet.as_view()),
    path("<int:pk>", views.AnimalViewSet.as_view()),
    path("<int:pk>/follow", views.AnimalFollowViewSet.as_view()),
    path("<int:pk>/unfollow", views.AnimalUnfollowViewSet.as_view()),
]
