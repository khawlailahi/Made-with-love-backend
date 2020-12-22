# from django import path 
from .views import signupSeller
from .views import signupBuyer
from django.urls import path
urlpatterns = [
    path('seller/signup', signupSeller.as_view(),),
    path('buyer/signup', signupBuyer.as_view(),)
]