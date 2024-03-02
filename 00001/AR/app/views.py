from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Это тестовая страница нашей выпускной работы!!!")

def about(request):
    return render(request,'app/about.html',{'title':'О нас'}) 