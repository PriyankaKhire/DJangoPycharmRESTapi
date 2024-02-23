from django.urls import path

from mywebapp import views

urlpatterns = [
    path('', views.MyWebAppView.as_view()), # Don't forget the comma
    path('getAllAlphabets', views.GetAllNamesView.as_view()),
    path('getNameById', views.GetAlphabetByIdView.as_view())
]