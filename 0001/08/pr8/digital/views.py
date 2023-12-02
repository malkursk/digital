from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Добро пожаловать на главную!")