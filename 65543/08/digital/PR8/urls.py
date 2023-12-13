
from django.urls import path

from PR8.views import *

urlpatterns = [
    path('', MyFunction),
    path('02/', func02),
    path('03/', func03),
    path('calc/<str:val>', calc),
    path('country/city/<int:val>', r01),
]
