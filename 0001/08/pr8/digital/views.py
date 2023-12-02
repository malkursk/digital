from django.shortcuts import redirect, render, HttpResponse
from digital.utils import converter

def main(request):
    return HttpResponse("Добро пожаловать на главную!") 

def page02(request):
    return render(request, '02/index.html')

def page03(request):
    return render(request, '03/index.html')

def calc(request, val):
    return HttpResponse(f"{val}, {converter(val)}")

def page08(request, val):
    return HttpResponse(f"Цвет обоев в Вашей новой комнате: {val}")

def pageNotFound(request, exception):
    return HttpResponse("<h1>Что-то пошло не так</h1>")