# from django import path 
from .views import signupSeller
from .views import Login
from .views import signupBuyer
from .views import Login
from django.urls import path
from .views import comment
from .views import getcomments
from .views import deleteComment
from .views import mostPopuler

urlpatterns = [
    path('seller/signup', signupSeller.as_view(),),
    path('buyer/signup', signupBuyer.as_view(),),
    path('login', Login.as_view(),),
    path('deleteComment/<int:pk>', deleteComment.as_view(), ),
    path('getcomments/<int:id>', getcomments.as_view(), ),
    path('comment', comment.as_view(),),
    path('populer', mostPopuler.as_view(),)

]
