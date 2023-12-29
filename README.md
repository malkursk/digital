# Digital
## Проект для обучения

### Маршрутизация на базе Flask
1. Создание виртуального окружения: python -m venv .venv
2. Его активация (деактивация): .venv\Scripts\activate (deactivate)
3. Установка зависимостей: pip install Flask
4. Запуск проекта: flask --app main run
#### Повторный запуск (после перезапуска IDE или неактивном venv) - п.2, п.4

### Маршрутизация на базе Django
1. Создание виртуального окружения: python -m venv .venv
2. Его активация (деактивация): .venv\Scripts\activate (deactivate)
3. Установка зависимостей: pip install Django
4. Переход в папку с основным проектом: cd projectName
5. Запуск проекта: python manage.py runserver
#### Повторный запуск (после перезапуска IDE или неактивном venv) - п.2, п.4, п.5

выгрузка-загрузка данных:
python manage.py dumpdata my.Account  > .\my\seeders\accounts.json
python manage.py loaddata  .\my\seeders\accounts.json
