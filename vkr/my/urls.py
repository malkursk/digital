
from django.urls import include, path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'test', TestViewSet)


urlpatterns = [
    path('', list,name='url_list'), 
    path('create',  create, name='url_create'),  
    path('edit/<int:id>',  update),   
    path('delete/<int:id>',  destroy), 

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))     
]