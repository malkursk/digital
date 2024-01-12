from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += [    
    path('admin/', admin.site.urls),
    path('', include('my.urls')),
    path('demo/', include('admin_soft.urls')),
]
