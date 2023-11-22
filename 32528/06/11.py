#def pr6_1
name=input('Имя:')
print('Привет,' + name +  '!')
year=int(input('Год рождения:'))
if(2023-year)>21:
    s='у Вас прекрасный возраст'
else:
    if(2023-year)<21:
         s='Вам нужно ещё немного времени'
    else:
         s='Вы в норме'
    print (name +',' +s)