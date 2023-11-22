def pr6_task1():
    name = input('Имя:')
    print('Дарова,'+ name + '!')
    year=int(input('Год рождения:'))
    if(2023-year)>20:
        s= 'у Вас прекрасный возраст'
    else:
        if(2023-year)<20:
            s= 'Вам нужно еще немного времени'
        else:
            s= 'Вы в норме '

    return name + ', ' + s        

def pr6_task2():
    p1 = 'Иванов Илья 2002'
    p2 = 'Брезинский Виктор 2003'
    p3 = 'Том Хохланд 1998'


    m1 = p1.split()
    m2 = p2.split()
    m3 = p3.split()

    m = [ m1[1]+' '+ m1[0], m2[1]+' '+m2[0], m3[1]+' '+m3[0] ]

    m.sort()

    m1 = m[0].split()
    m2 = m[1].split()
    m3 = m[2].split()

    return m1[1],m2[1],m3[1]

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

def Elka():
    v = int(input('Ширина ветки:'))
    n = int(input('Кол-во:'))
    res = ''
    for j in range(0,n):
        s = '' 
        for i in range(0,v):
            s+= '*'
            res+='s\n'
            print(s)
    return 'Проведи Новый год с пользой!'


def main(): 
    print('Выполнил: Сушков Даниил, 44-22-167') 
 
    again = True 
    while again: 
        n = input('введите номер задания, который надо выполнить (1,2,3,4): ') 
        res = 'тут будет результат' 
        if n == '1': 
            res = pr6_task1() 
        if n == '2': 
            res = pr6_task2() 
        if n == '3': 
            res = pr6_task3(6,22) 
        if n =='4':
            res = Elka()
        print(res) 
        if input('Если надо ещё разок - жми пробел + enter') != ' ': 
            again = False 
            print('ББ') 
            
 


main()

