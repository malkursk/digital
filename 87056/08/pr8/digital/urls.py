from django.urls import *

from digital.views import *


urlpatterns= [
     path('', index),
    path('02', page02),
    path('03', page03),
    path('calc/<str:val>', calc),
    path('material/color/<slug:val>', p8)
]