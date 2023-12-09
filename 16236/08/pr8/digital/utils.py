def converter(v,b1=10,b2=16):
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
    return f'{number}, (base: {b1}) =>Результат (base {b2}) = {result} (base {b1})'