# from django import path 
from .views import signup
from .views import addItem

from django.urls import path
urlpatterns = [
    path('signup', signup.as_view(),),
    path('addItem', addItem.as_view(),)
]