from django.http import HttpResponse
from django.shortcuts import render, redirect
from digital.fun import converter
# Create your views here.
def index(request):
    return HttpResponse("Якунин Алексей Владимирович 44-23-169")
def page02(request):
    return render(request,'lab2/index.html')
def page03(request):
    return render(request,'lab3/index2.html')
def calc(request, val):
    return HttpResponse(f"{converter(val)}")

def pageNOTfound(request, exception):
    return HttpResponse(f"<h1>Что-то пошло не так</h1>")

def p8(request, val):
    return HttpResponse(f"Цвет обоев в Вашей комнате: {val}")
