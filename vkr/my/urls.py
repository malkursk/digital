
from django.urls import path
from my.views import *

urlpatterns = [
    path('', main),
    path('test/<str:val>', test),
    path('create', create, name='url_create'),  
    path('list',list,name='url_list'), 
    path('edit/<int:id>', update),   
    path('delete/<int:id>', destroy),  

]