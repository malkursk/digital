from django.shortcuts import render
from django.shortcuts import redirect, render
from Planets.models import *

def about(request): 
    return render(request,'Planets/layout.html') 

def list(request): 
    return render(request,'Planets/home.html',{'data':Planets.objects.all()}) 

def detail(request, planet_id):
    planets = Planets.objects.get(id=planet_id)
    return render(request, 'Planets/planetdetail.html', {'planets': planets})


# Create your views here.
