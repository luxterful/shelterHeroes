from django.urls import include, path

from ShelterHeroesServer.api.core.posts import views

app_name = "posts"

urlpatterns = [
    path("<int:pk>", views.PostViewSet.as_view()),
    path("<int:pk>/like", views.PostLikeViewSet.as_view()),
    path("<int:pk>/unlike", views.PostUnlikeViewSet.as_view()),
    path("<int:pk>/comments", views.PostCommentViewSet.as_view()),
]
