

from django.urls import path
from pr8.views import *

urlpatterns = [
    
    path('start/', myFunction),
    path('02/', func02),
    path('03/', func03),
    path('calc/<str:val>', calc)
]

