from django.shortcuts import render, HttpResponse


def pageNotFound(request, exception): 
    return HttpResponse("<h1>Что-то пошло не так</h1>")

def myfunction(request):
    return HttpResponse("<h1> Привет от коти! </h1> Практическая работа №8. Костинова Мария гр.44-23-167") 

def func02(request):
    return render(request, "02/index.html") 


def func03(request):
    return render(request,"03/index.03.html") 

def r01(request, val):
    return HttpResponse(f"Вы выбрали город №:{val}") 


def calc(request, val):
   return HttpResponse(converter(val)) 

def converter(v,b1=17,b2=12): 
    try: 
        number = int(v,b1) 
    except: 
        return 'Неверное число' 
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    if number == 0: 
        return '0' 
    result = [] 
    while number>0: 
        number, mod = divmod(number, b2) 
        result.append(digits[mod]) 
    result = ''.join(reversed(result)) 
    return f'{v}, (base: {b1}) => {result} (base: {b2})'