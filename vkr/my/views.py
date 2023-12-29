from django.shortcuts import redirect, render, HttpResponse

from django.http import HttpResponse

def main(request):
    return HttpResponse("Успешный запуск сервиса")

def test(request, val):
    return HttpResponse(f"Тестовый параметр: {val}")
