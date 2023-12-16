from django.shortcuts import render, HttpResponse
from pr8.utils import converter

def myFunction(request):
    return HttpResponse('Практическая работа 8 Супрун Анна Юрьевна 44-23-171')
def func02(request):
    return render(request,"02/index.html")
def func03(request):
    return render(request,"03/index.html")
def calc(request, val):
    return HttpResponse(converter (val))
def arts(request, val):
    return HttpResponse(f"Сегодня выступает: {val}")
def country(request, val):
    return HttpResponse(f"Температура выше нуля на: {val}")
def sport(request, val):
    return HttpResponse(f"Мой любимый вид спорта: {val}")
def pagenotfound (request, exception):
    return HttpResponse ("Упс... Здесь ничего нет")




