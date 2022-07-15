from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_simplejwt import views as jwt_views
from .views import *


urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/customers/', CustomersTokenObtainPairView.as_view(), name='Customers_token'),
]