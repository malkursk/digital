# Digital
    Demo project for students

## Step 0. Init virtuel env
    python -m venv .venv

## Step 1. To activate venv windows/linux
    .\.venv\Scripts\activate
    source .venv/bin/activate

use PowerShell by admin and  execute: 
    Set-ExecutionPolicy RemoteSigned
    A (comfirm for ALL)

## Step 2. To save packages
    pip freeze >package.txt

## Step 3. To deactivate a virtual environment:
    deactivate

## Step 4. To init from req    
    virtualenv .venv
    Step 1 (windows/linux)
    pip install -r package.txt

## to install new packages
    pip install <package-name>


### CUSTOM in Russian:
----------------------------------------
## Практическая работа №7
# Для ПЕРВОГО запуска проекта выполнить этапы:

# 1. Создать виртуальное окружения
python -m venv .venv

# 2. Его активация
.\.venv\Scripts\activate

# 3. Установка поддержки Django
pip install Flask

# 4. Запустить сервер
flask --app main run

# Повторный запуск после перезапуска IDE или неактивном venv - выполнение п.2, п.4

----------------------------------------
## Практическая работа №8
# Для ПЕРВОГО запуска проекта выполнить этапы:

# 1. Создать виртуальное окружения
python -m venv .venv

# 2. Его активация
.\.venv\Scripts\activate

# 3. Установка поддержки Django
pip install Django

# 4. Перейти в папку с основным проектом
cd <projectName>

# 5. Запустить сервер
python manage.py runserver

# Повторный запуск после перезапуска IDE или неактивном venv - выполнение п.2, п.4, п.5