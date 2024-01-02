
from django.urls import path
from my.views import *

urlpatterns = [
    path('', main),
    path('test/<str:val>', test),
    path('create', create),  
    path('list',list), 
    path('edit/<int:id>', update),   
    path('delete/<int:id>', destroy),  

]