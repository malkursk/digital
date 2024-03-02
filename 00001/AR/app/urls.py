from django.urls import path

from . import views

urlpatterns = [
    path("", views.cards_page, name="cards"),
    path('create',  views.create, name='create'),  
    path('preview/<id>',  views.preview, name="preview"),       
    path('update/<id>',  views.update,name="update"),   
    path('delete/<int:id>',  views.destroy, name="destroy"),     
    path("about", views.about, name="about"),
]