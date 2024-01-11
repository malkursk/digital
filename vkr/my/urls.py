
from django.urls import include, path

from my.utils.excel_proc import export_to_excel
from .views import *
from rest_framework import routers


urlpatterns = [    
    path('model_to_excel/<str:v>', export_to_excel),  
]


