
from django.urls import path
from digital.views import *

urlpatterns = [
    path('02/', page02),
    path('03/', page03),
    path('', main),
    path('calc/<str:val>/', calc)
]