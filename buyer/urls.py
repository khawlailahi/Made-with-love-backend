
from .views import getCategoryItems
from .views import orderItem
from django.urls import path
from django.urls import include, re_path
# ---> add here the rest of the url 
# path('', signupSeller.as_view(),)

from .views import buyer_username
from .views import buyer_password
from .views import buyer_location
from .views import buyer_number
from .views import get_all
from .views import rate

urlpatterns = [
    path('userName', buyer_username.as_view(), ),
    path('location', buyer_location.as_view(), ),
    path('changePassword', buyer_password.as_view()),
    path('order', order_item.as_view(), ),
    path('<slug:cat>', get_category_items.as_view(), ),
    path('getAll/' , get_all.as_view(),),
    path('phoneNumber/', buyer_number.as_view(),),
    path('ratingg/', rate.as_view(),)

 ]