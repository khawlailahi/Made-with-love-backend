#  here import function like this :      from .views import functionfromview
from django.urls import path
# ---> add here the rest of the url 
    # path('', signupSeller.as_view(),)
from .views import addItem
urlpatterns = [
 path('addItem', addItem .as_view(), )]