
from django.urls import path
from my.views import *

urlpatterns = [
    path('', main),
    path('test/<str:val>', test),

]