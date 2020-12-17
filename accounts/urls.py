# from django import path 
from .views import signup
from django.urls import path
urlpatterns = [
    path('/signup', signup.as_view(),)
]