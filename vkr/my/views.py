from django.shortcuts import redirect, render
from django.http import HttpResponse
from my.forms import *
from my.models import *
from rest_framework import viewsets


def create(request):  
    if request.method == "POST":  
        form = TestForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/list')  
            except:  
                pass
    else:  
        form = TestForm()  
    return render(request,'my/create.html',{'form':form})  

def list(request):  
    data = Test.objects.all()  
    return render(request,'my/list.html',{'data':data}) 

def update(request, id):  
    data = Test.objects.get(id=id)  
    form = TestForm(request.POST, instance = data)  
    if form.is_valid():  
        form.save()  
        return redirect("/list")  
    return render(request, 'my/edit.html', {'data': data})  

def destroy(request, id):  
    data = Test.objects.get(id=id)  
    data.delete()  
    return redirect("/list")   


from my.serializers import TestSerializer
from my.models import Test

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all().order_by('updated_at')
    serializer_class =TestSerializer