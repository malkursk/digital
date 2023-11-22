def pr6_task3(b1,b2): 
    v = input(f'Исходное число (base {b1}) = ') 
    if not (v and b1 and b2): 
        return 'ошибка ввода' 
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
    return f'Результат (base {b2}) = {result}'

res = pr6_task3(15,11)
print(res)