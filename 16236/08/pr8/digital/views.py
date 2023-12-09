#from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

from digital.utils import converter

def index(request):
    return HttpResponse ("<h1>Добро пожаловать на главную!</h1>") 
def page02(request):
    return HttpResponse ("<h1>Вы попали на вторую лабу!</h1>") 
#def page03(request):
    #return HttpResponse ("<h1>Вы попали на третью лабу!</h1>") 



def page03(request):
    return render (request, '03/index.html')

def calc(request, val):
    return HttpResponse (f" {converter(val)}</h1>")


def pageNotFound (request,exception):
    return HttpResponse ("<h1>Данная страница не найдена!</h1>")

