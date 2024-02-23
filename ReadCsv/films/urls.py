from django.urls import path

from films import views

urlpatterns = [
    path('', views.FilmList.as_view()),
]