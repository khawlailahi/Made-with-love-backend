from django.conf.urls import url
from payments import views
from .views import Payment_view
urlpatterns = [
    url('checkout',  Payment_view.as_view(), ),
]