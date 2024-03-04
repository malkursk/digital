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

