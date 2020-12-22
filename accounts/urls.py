# from django import path 
from django.contrib import admin
from django.urls import path, include , re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView


# urlpatterns = [
#  path('/seller', include('seller.urls')),]