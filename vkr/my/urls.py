
from django.urls import include, path

from my.utils.excel_proc import export_to_excel
from .views import import_person_from_excel


urlpatterns = [    
    path('model_to_excel/<str:v>', export_to_excel),  
    path('excel_to_person', import_person_from_excel),  
]


