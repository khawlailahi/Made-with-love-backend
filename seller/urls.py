#  here import function like this :      from .views import functionfromview
from django.urls import path
from django.urls import include, re_path
from .views import getCategoryStore
from .views import addItem
urlpatterns = [
 path('addItem', addItem .as_view(), ),
 path('<slug:cat>', getCategoryStore.as_view(), )
 ]