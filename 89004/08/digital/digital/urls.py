
#from PR8.views import pageNotFound
from django.contrib import admin
from django.urls import include, path

from PR8.views import *
handler404 = pageNotFound
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('PR8.urls')),
    
]
