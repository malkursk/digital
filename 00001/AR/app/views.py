from django.shortcuts import render
from django.http import HttpResponse

from app.models import News
from django.core import serializers
import json
from django.core.paginator import Paginator


def index(request):
    return HttpResponse("Это тестовая страница нашей выпускной работы!!!")

def about(request):
    return render(request,'app/about.html',{'title':'О нас'}) 

def preview(request, id):
    data = serializers.serialize("json", [News.objects.get(id=id)] )[1:-1]
    data = json.loads(data)
    return render(request, 'app/element.html', {'form': data, 'title':'Просмотр, id:' + id})    

def cards_page(request):
    contact_list = News.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "app/cards.html", {"data": page_obj})