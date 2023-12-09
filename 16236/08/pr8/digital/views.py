
from django.shortcuts import render, HttpResponse
# from http.shortcuts import HttpResponse


def main(request):
    return HttpResponse("<h1>Добро пожаловать на главную!</h1>")

def page02(request):
    return render("<h1>Лаба 2</h1>")

def page03(request):
    return render("<h1>Лаба 3</h1>")