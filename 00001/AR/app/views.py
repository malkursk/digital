from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import NewsForm
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
    paginator = Paginator(contact_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "app/cards.html", {"data": page_obj})

def update(request, id):
    data = News.objects.get(id=id)  
    form = NewsForm(request.POST or None, instance = data)
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'app/element.html', {'form': form, 'title':'Редактор, id:' + id,'route': '/update/'+id})  

def destroy(request, id):  
    data = News.objects.get(id=id)  
    data.delete()  
    return redirect("/")

def create(request):  
    if request.method == "POST":  
        form = NewsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = NewsForm()  
    return render(request,'app/element.html',{'form':form, 'title':'Новая запись','route': '/create'})  