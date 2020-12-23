#  here import function like this :      from .views import functionfromview
from django.urls import path
# ---> add here the rest of the url 
    # path('', signupSeller.as_view(),)
from .views import addItem
from .views import SnippetDetailSeller


urlpatterns = [
 path('addItem', addItem.as_view()),
 path('delete/<int:pk>/', SnippetDetailSeller.as_view()),
 path('editProfile', SnippetDetailSeller.as_view()),
 path('profile/<int:pk>', SnippetDetailSeller.as_view())
 
 ]


