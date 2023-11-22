name=input('Имя:')
year=int(input('Год рождения:'))
if(2023-year)>21:
    s='у Вас прекрасный возраст'
else:
    if(2023-year)<21:
        s='Вам нужно ещё немного времени'
    else:
        s='Вы в норме'
#return name +',' +s