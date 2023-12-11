
from django.contrib import admin
from django.urls import path
from pr8.views import *
handler404 = pagenotfound

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',myFunction),
    path ('02',func02),
    path ('03',func03),
    path ('calc/<str:val>',calc),
    path ('arts/artists/<str:val>',arts),
    path ('music/singer/<int:val>',music),
    path ('sport/tournament/<str:val>',sport)

]
