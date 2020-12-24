
from .views import getCategoryItems
from django.urls import path
from django.urls import include, re_path
# ---> add here the rest of the url 
# path('', signupSeller.as_view(),)

urlpatterns = [
 path('<slug:cat>', getCategoryItems.as_view(), )]