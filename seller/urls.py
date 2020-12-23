#  here import function like this :      from .views import functionfromview
from django.urls import path
from django.urls import include, re_path
from .views import getCategoryStore
from .views import addItem
from .views import SnippetDetailSeller
from .views import getItems
from .views import getItemsVisit
from .views import sellerVisit


urlpatterns = [
<<<<<<< HEAD
 path('addItem', addItem.as_view()),
 path('delete/<int:pk>/', SnippetDetailSeller.as_view()),
 path('editProfile', SnippetDetailSeller.as_view()),
 path('profile/<int:pk>', SnippetDetailSeller.as_view()),
 path('profile/items/<int:pk>', getItems.as_view()),
 path('visit/items/<int:pk>', getItemsVisit.as_view()),
 path('visit/<int:pk>', sellerVisit.as_view())
 
 ]


=======
 path('addItem', addItem .as_view(), ),
 path('<slug:cat>', getCategoryStore.as_view(), )
 ]
>>>>>>> 2fb8cb1807c4388b53f8ac2e4fc5040cd110df54
