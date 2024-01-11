
from django.urls import include, path

from my.utils.excel_proc import export_to_excel
from .views import import_person_from_excel

from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'sport', views.SportViewSet)
router.register(r'person', views.PersonViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]

urlpatterns += [    
    path('test', views.test),      
]

urlpatterns += [    
    path('model_to_excel/<str:v>', export_to_excel),  
    path('excel_to_person', import_person_from_excel),  
]


