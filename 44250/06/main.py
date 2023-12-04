def pr6_task1():
    name = input ('Имя:')
    year = int(input('Год рождения:'))
    if (2023 - year)>21:
        s= ',у Вас прекрасный возраст'
    else:
        if (2023 - year)<21:
            s= ',Вам нужно еще немного времени'
        else:
            s= ',Вы в норме'
    return name + ',' + s




def pr6_task2():
    p1 = input ('друг 1:')
    p2 = input ('друг 2:')
    p3 = input ('друг 3:')   

    m1 = p1.split( )
    m2 = p2.split( )
    m3 = p3.split( )

    m = [m1[1]+' '+m1[0],m2[1]+' '+m2[0],m3[1]+' '+m3[0]]

    m.sort()

    m1 = m[0].split()
    m2 = m[1].split()
    m3 = m[2].split()
    return m1[1]+' '+m2[1]+' '+m3[1]


def pr6_task3(b1, b2):
    v = input (f'исходное число (base{b1})=')
    if not (v and b1 and b2):
        return 'ошибка ввода'
    try: 
        number = int (v,b1)
    except:
        return 'неверное число'
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number == 0:
        return '0'
    result = []
    while number>0:
            number, mod = divmod (number, b2)
            result. append (digits[mod])
    result = ''.join(reversed(result))
    return f'результат (base{b2})={result}'



def elka():
    v = int (input ('ширина ветки: '))
    n= int (input ('количество веток: '))
    res= ' '
    for j in range (0,n):
        s = ' '
        for i in range (0,v):
            s +='*'
            res+= 's\n'
            print (s)
    return 'с Новым Годом!'



def main():
    print('Выполнила Тарабарова Марина Александровна, 44-23-171')
    again=True
    while again:
        n=input('Введите номер задания, который Вы хотите выполнить(1,2,3,4):')
        res='Тут будет результат'
        if n=='1':
            res=pr6_task1()
        if n=='2':
            res=pr6_task2()
        if n=='3':
             res=pr6_task3(8, 10)
        if n=='4':
            res=elka()
        print(res)
        if input ('Для того, чтобы выполнить программу еще раз, нажми пробел+enter') !=' ':
            again=False
            print ('Спасибо за внимание!')

main()
