from django.contrib import admin
from django.urls import path
from profiles_api import views
urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('s-view/',views.snippetView.as_view()),
]
