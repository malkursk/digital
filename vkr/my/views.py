from django.shortcuts import redirect, render
from django.http import HttpResponse
from my.forms import *
from my.models import *

def main(request):
    return HttpResponse("Успешный запуск сервиса")

def test(request, val):
    return HttpResponse(f"Тестовый параметр: {val}")

def create(request):  
    if request.method == "POST":  
        form = TestForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/list')  
            except:  
                {{ form.errors }}
    else:  
        form = TestForm()  
    return render(request,'create.html',{'form':form})  

def list(request):  
    data = Test.objects.all()  
    return render(request,'list.html',{'data':data})  

