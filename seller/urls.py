from django.urls import path
from django.urls import include, re_path
from .views import get_category_store
from .views import add_item
from .views import snippet_detail_seller
from .views import get_items
from .views import get_items_visit
from .views import seller_visit
from .views import get_list_order
from .views import delete_item
from .views import seller_password
from .views import seller_storename
from .views import seller_location
from .views import seller_delivery
from .views import seller_image
from .views import seller_description
from .views import edit_item
from .views import get_all
from .views import get_rate

urlpatterns = [
 path('changePassword', seller_password.as_view()),
 path('editProfile/<int:pk>', edit_item.as_view(), ),
 
  # for changing setting for the seller 
 path('storeName', seller_storename.as_view()),
 path('location', seller_location.as_view()),
 path('description', seller_description.as_view()),
 path('delivery', seller_delivery.as_view()),
 path('image', seller_image.as_view()),

 path('addItem', add_item.as_view(), ),   
 path('<slug:cat>', get_category_store.as_view(), ), 
 path('rate/<int:pk>' , get_rate.as_view(),),
 path('profile/deleteitems/<int:pk>', delete_item.as_view(), ),
 path('editProfile', snippet_detail_seller.as_view()),
 path('profile/<int:pk>', snippet_detail_seller.as_view()),
 path('profile/items/<int:pk>', get_items.as_view()),
 path('visit/items/<int:pk>', get_items_visit.as_view()),
 path('visit/<int:pk>', seller_visit.as_view()),
 path('getAll/' , get_all.as_view(),),
 path('order/list/<int:pk>', get_list_order.as_view(), ),

 ]
