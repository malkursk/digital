def pr6_task1():
    name = input('Имя: ')
    year = int(input('Год рождения: '))
    if (2023-year)>21:
        s = 'у Вас прекрасный возраст'    
    else:
        if (2023-year)<21:
            s = 'Вам нужно еще немного времени'        
        else:
            s = 'Вы в норме'
    return name + ', ' +s

def pr6_task2():
    p1 = input('друг 1: ')
    p2 = input('друг 2: ')
    p3 = input('друг 3: ')

    m1 = p1.split()
    m2 = p2.split()
    m3 = p3.split()

    m = [ m1[1]+' '+m1[0], m2[1]+' '+m2[0], m3[1]+' '+m3[0] ]

    m.sort()

    m1 = m[0].split()
    m2 = m[1].split()
    m3 = m[2].split()

    return m1[1] + ' ' + m2[1] + ' ' + m3[1]

def pr6_task2_clever():
    n = int(input('количество друзей: '))    
    print(f'строгий формат: ИМЯ пробел ГОД РОЖДЕНИЯ')
    m = []
    result = ''
    for i in range (0,n):
        s = ' '.join(list(reversed(input(f'Друг {i+1}: ').split())))
        m.append(s)
    m.sort(reverse = False)
    for i in range (0,n):
        result += m[i].split()[1] + ' '        
    return 'По возрастанию г.р.: ' + result

def pr6_task3(b1,b2):
    v = input(f'Исходное число (base {b1}): ')
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

def elka():
    v = int(input('Ширина ветви: '))
    n = int(input('Количество: '))    
    res = ''
    for j in range(0,n):
        s=''
        for i in range(0,v):
            s+='*'
            res+='s\n'
            print(s)
    return 'скоро Новый год!'


def main():
    print('Выполнил: Якунин Алексей Владимирович, гр. 44-22-169 (87056)')

    again = True
    while again:
        n = input('Режим: 0-Ёлка, 1-Сравнение, 2-Сортировка, 3-Конвертер. Ваш выбор: ')
        res = 'тут будет результат'
        if n == '0':
            res = elka()        
        if n == '1':
            res = pr6_task1()
        if n == '2':
            res = pr6_task2()
        if n == '3':
            res = pr6_task3(2,10)
        if n == '4':
            res = pr6_task2_clever()            
        print(res)
        if input('Введите 8 для повтора или другой символ для выхода: ') != '8':
            again = False
            print('Спасибо за внимание!')

main()