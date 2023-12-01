def pr6_task1():
 print("Ваше имя:")
 name=input()
 print("Год рождения:")
 year=input()
 if year.isnumeric():
    year=int(year)
    if not(1899<year<2023):
        print("Мы не работаем с такими пользователями")
        exit()
    age=2023-year - 1
    print("Ваш возраст:" + str(age-1) + " или "+str(age))
    if age> 20:
     print("У Вас прекрасный возраст")
    else:
     if age< 20:
       print("Вам нужно еще немного времени")
     else:
      print ("Вы в норме")
 else: 
    print("Ошибка")


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

def main():
    print('Выполнила: Корнева Арина Александровна, гр. 44-23-170 (06)')

    again = True
    while again:
        n = input('Режим: 1-Сравнение, 2-Сортировка, 3-Конвертер. Ваш выбор: ')
        res = 'тут будет результат' 
        if n == '1':
            res = pr6_task1()
        if n == '2':
            res = pr6_task2()
        if n == '3':
            res = pr6_task3(10,2)        
        print(res)
        if input('Введите 8 для повтора или другой символ для выхода: ') != '8':
            again = False
            print('Спасибо за внимание!')

main()

