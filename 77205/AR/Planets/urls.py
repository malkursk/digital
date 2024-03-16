from django.urls import include, path
from .views import *

urlpatterns = [
    path('', about, name='url_list'), 
    path('planets', list, name='ul_list'),
    path('planets/<int:planet_id>/', detail, name='detail')

]