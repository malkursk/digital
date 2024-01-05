from django.shortcuts import redirect, render
from django.http import HttpResponse
from my.forms import *
from my.models import *
from rest_framework import viewsets
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required


@login_required
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

def list(request): 
    return render(request,'my/list.html',{'data':Test.objects.all()}) 

def preview(request, id):
    data = serializers.serialize("json", [Test.objects.get(id=id)] )[1:-1]
    data = json.loads(data)
    return render(request, 'my/element.html', {'form': data, 'title':'Просмотр, id:' + id})      

@login_required
def update(request, id):
    data = Test.objects.get(id=id)  
    form = TestForm(request.POST or None, instance = data)
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'my/element.html', {'form': form, 'title':'Редактор, id:' + id,'route': '/update/'+id})  

@login_required
def destroy(request, id):  
    data = Test.objects.get(id=id)  
    data.delete()  
    return redirect("/")   

from django.shortcuts import render
from openpyxl import load_workbook

@login_required
def import_from_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        wb = load_workbook(excel_file)
        ws = wb.active
        for row in ws.iter_rows(min_row=2, values_only=True):
            login = row[2]
            passw = row[3]
            if login and passw:                
                if not Account.objects.filter(login=login):
                    Account.objects.create(login=row[2], passw=row[3], busy=False)
        return HttpResponse("Импорт завершен") 
    return render(request, 'my/import_form.html')


from my.serializers import TestSerializer
from my.models import Test

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all().order_by('updated_at')
    serializer_class =TestSerializer