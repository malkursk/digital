from django.shortcuts import redirect, render
from django.http import HttpResponse
from my.forms import *
from my.models import *
from rest_framework import viewsets
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required

def create(request):  
    if request.method == "POST":  
        form = TestForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = TestForm()  
    return render(request,'my/element.html',{'form':form, 'title':'Новая запись','route': '/create'})  

@login_required
def list(request):  
    return render(request,'my/list.html',{'data':Test.objects.all()}) 

def preview(request, id):
    data = serializers.serialize("json", [Test.objects.get(id=id)] )[1:-1]
    data = json.loads(data)
    return render(request, 'my/element.html', {'form': data, 'title':'Просмотр, id:' + id})      

def update(request, id):
    data = Test.objects.get(id=id)  
    form = TestForm(request.POST or None, instance = data)
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'my/element.html', {'form': form, 'title':'Редактор, id:' + id,'route': '/update/'+id})  

def destroy(request, id):  
    data = Test.objects.get(id=id)  
    data.delete()  
    return redirect("/")   


from my.serializers import TestSerializer
from my.models import Test

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all().order_by('updated_at')
    serializer_class =TestSerializer