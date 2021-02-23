# from django import path 
from .views import signup_seller
from .views import login
from .views import signup_buyer
from django.urls import path
from .views import comment
from .views import get_comments
from .views import delete_comment
from .views import most_populer

urlpatterns = [
    path('seller/signup', signup_seller.as_view(),),
    path('buyer/signup', signup_buyer.as_view(),),
    path('login', login.as_view(),),
    path('deleteComment/<int:pk>', delete_comment.as_view(), ),
    path('getcomments/<int:id>', get_comments.as_view(), ),
    path('comment', comment.as_view(),),
    path('populer', most_populer.as_view(),)

]
