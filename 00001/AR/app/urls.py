from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path("", views.cards, name="cards"),
    path('create',  views.create, name='create'),  
    path('preview/<id>',  views.preview, name="preview"),       
    path('update/<id>',  views.update,name="update"),   
    path('delete/<int:id>',  views.destroy, name="destroy"),     
    path('about', views.about, name="about"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Цифровая кафедра",
      default_version='v 1.0',
      description="Описание серверных функций",
   ),
)

urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]