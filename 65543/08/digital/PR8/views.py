from django.shortcuts import render, HttpResponse

def pageNotFound(request, exception): 
    return HttpResponse("Будьте внимательнее, все роуты  прописаны в методичке!")

def MyFunction(request):
    return HttpResponse("Привет от Зиминой Екатерины Александровны! гр. 44-23-167 Лабораторная работа №8")

def func02(request):
    return render(request, "02/index.html")

def func03(request):
    return render(request, "03/index.html")

def r01(request, val):
    return HttpResponse(f"Вы выбрали город:{val}")


def calc(request, val):
    return HttpResponse (converter(val))
    

def converter(v,b1=15,b2=11): 
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

