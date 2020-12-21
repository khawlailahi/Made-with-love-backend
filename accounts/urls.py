# from django import path 
from .views import signupSeller
from django.urls import path
urlpatterns = [
    path('buyer/signup', signupSeller.as_view(),)
    
]