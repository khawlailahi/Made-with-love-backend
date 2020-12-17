"""madewithlove URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include , re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/',  TokenRefreshView.as_view(), name= 'token_refresh'),


    # this is the url for the signup (/accounts/seller/signup)
    path('accounts/seller', include('accounts.urls')),

    path('admin/', admin.site.urls),
]
static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += [re_path('^.*', TemplateView.as_view(template_name= 'index.html'))]
