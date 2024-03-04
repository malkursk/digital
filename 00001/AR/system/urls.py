
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
]


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns += [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify', TokenVerifyView.as_view(), name='token_verify'),
]
