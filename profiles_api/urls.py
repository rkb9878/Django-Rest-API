from django.urls import path,include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')

urlpatterns = [
    # API view
    path('hello-view/',views.HelloApiView.as_view()),
    path('s-view/', views.snippetView.as_view()),

    # viewset
    path('',include(router.urls)),


]
