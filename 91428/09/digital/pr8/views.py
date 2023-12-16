from django.shortcuts import render, HttpResponse
from pr8.utils import converter 

def myFunction(request):
    return HttpResponse('Практическая работа 8 Александра Рубцова 44-23-171')

def func02(request):
    return render(request,"02/index.html")

def func03(request):
    return render(request,"03/index.html")

def calc(request, val):
    return HttpResponse(converter(val))