print('программа 1')
print('Введите Имя')
name = input ()
print('Какое у Вас необычное имя, ' + name)
print('Введите год рождения')
year = input()
if year.isnumeric():
    year = int(year)
    if (1990>year or year>2023):
        print('Ошибка')
    age = 2023 - year
    print('Ваш возраст  ' + str(age))
    if age < 20:
         print(name + ' You molod')
    else:
        if age > 20:
          print(name + ' You star')
        else:
           print(name + ' You vary good')
else:
    print('Ошибка')