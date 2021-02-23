
from django.contrib import admin
from django.urls import path, include , re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',  TokenRefreshView.as_view(), name= 'token_refresh'),
    # this is the url for the signup (/accounts/seller/signup)

    # this is the url for seller
    path('', include('accounts.urls')),
  # this is the url for buyer
    path('seller/', include('seller.urls')),
    # this is the url for seller
    path('buyer/', include('buyer.urls')),
    path('payments/', include('payments.urls')),

    path('admin/', admin.site.urls),
]
static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += [re_path('^.*', TemplateView.as_view(template_name= 'index.html'))]
