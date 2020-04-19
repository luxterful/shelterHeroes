from django.urls import include, path

from ShelterHeroesServer.api.auth import views

app_name = "auth"

urlpatterns = [
    path("info/", views.AuthInfoView.as_view()),
    path("signup/", views.SignupView.as_view()),
    path("signin/", views.SigninView.as_view()),
    path("signout/", views.SignoutView.as_view()),
]
