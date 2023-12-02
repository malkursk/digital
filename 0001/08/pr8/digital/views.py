from django.shortcuts import render, HttpResponse
from digital.utils import converter

def main(request):
    return HttpResponse("Добро пожаловать на главную!") 

def page02(request):
    return render(request, '02/index.html')

def page03(request):
    return render(request, '03/index.html')

def calc(request, val):
    return HttpResponse(f"{converter(val)}")