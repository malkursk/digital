from django.shortcuts import render
from django.http import HttpResponse

from app.models import News
from django.core import serializers
import json


def index(request):
    return HttpResponse("Это тестовая страница нашей выпускной работы!!!")

def about(request):
    return render(request,'app/about.html',{'title':'О нас'}) 

def cards(request):
    return render(request,'app/cards.html',{'data':News.objects.all()}) 

def preview(request, id):
    data = serializers.serialize("json", [News.objects.get(id=id)] )[1:-1]
    data = json.loads(data)
    return render(request, 'app/element.html', {'form': data, 'title':'Просмотр, id:' + id})    
