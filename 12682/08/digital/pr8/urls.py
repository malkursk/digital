

from django.urls import path

from pr8.views import *

urlpatterns = [
    path('', myfunction ),
    path('02', func02 ),
    path('03', func03 ),
    path('calc/<str:val>', calc ),
    path('country/city/<int:val>', r01 ),
   # path('', pageNotFound )
]
