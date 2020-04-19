from django.urls import include, path
from ShelterHeroesServer.api.core.shelters import views

app_name = "shelters"

urlpatterns = [
    path("", views.ShelterListViewSet.as_view()),
    path("<int:pk>", views.ShelterViewSet.as_view()),
    path("<int:pk>/animals", views.AnimalListViewSet.as_view()),
    # path("/<int:pk>/follow", views.AnimalViewSet.as_view()),
    # path("/<int:pk>/unfollow", views.AnimalViewSet.as_view()),
]
