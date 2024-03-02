from django.urls import path

from . import views

urlpatterns = [
    path("", views.cards_page, name="cards"),
    # path('create',  create, name='url_create'),  
    path('preview/<id>',  views.preview),       
    # path('update/<id>',  update),   
    # path('delete/<int:id>',  destroy),     
    path("about", views.about, name="about"),
]