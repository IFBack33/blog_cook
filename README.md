<h2 align="center">Cook blog</h2>

**Ссылки**:
- [Telegram чат](https://t.me/IvanFilippochkin)

### Описание проекта:
Блог шеф-повара с рецептами


### Инструменты разработки

**Стек:**
- Python >= 3.9
- Django == 4.2.7
- sqlite3

## Разработка

##### 1) Поставить звездочку)


##### 2) Создать виртуальное окружение

    cd cook_blog
    
    python -m venv venv
    
##### 3) Активировать виртуальное окружение
    
Linux

    source venv/bin/activate
    
Windows

    ./venv/Scripts/activate

##### 4) Устанавливить зависимости:

    pip install -r req.txt

##### 5) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 6) Создать суперпользователя

    python manage.py createsuperuser
    
##### 7) Запустить сервер

    python manage.py runserver

##### 8) Ссылки

- Сайт http://127.0.0.1:8000/

- Админ панель http://127.0.0.1:8000/admin

## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2023-present, IFBack33 - Filippochkin Ivan
