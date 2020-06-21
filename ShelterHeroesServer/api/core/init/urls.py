from django.urls import include, path

from ShelterHeroesServer.api.core.init import views

app_name = "init"

urlpatterns = [
    path("initialize_data_random7747892874623737", views.InitViewset.as_view()),
]
