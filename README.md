# Мини библиотека

Данный проект был выполнен в качестве тестового задания для компании "ДЕЛИ"

## Installation

Клонировать репозиторий в любую папку

```bash
git clone https://github.com/AndreyKuskov/deli-test.git
```

Создать виртуальное окружение

```bash
python3 -m venv env
```

или 

```bash
python -m venv env
```

Активировать виртуальное окружение

```bash
. env/bin/activate
```

Перейти в папку проекта и выполнить команду

```bash
pip3 install -r requirements.txt
```

Перейдите в файл settings.py и настройте пункт DATABASES.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your_database_name>',
        'USER': '<your_user>',
        'PASSWORD': '<your_password_user>',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

Далее необходимо создать миграции для моделей приложения

```bash
python3 manage.py makemigrations library
```

Проводим миграции

```bash
python3 manage.py migrate
```

Запускаем проект
```bash
python3 manage.py runserver
```

## Email

andrey.kuskov.05@gmail.com