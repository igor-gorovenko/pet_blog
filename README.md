# Проект pet_blog

<img width="1024" alt="Screenshot 2023-06-21 at 14 24 18" src="https://github.com/igor-gorovenko/pet_blog/assets/59226858/796bed31-6906-4050-800c-bc6c99bb9cc3">

Превью проекта
#
## Инструкция по установке и запуску проекта

Скопируйте репозиторий
```
git clone git@github.com:igor-gorovenko/pet_blog.git
```

У вас должен быть установлен питон 3 версии, скачать можно тут: https://www.python.org/

Создаем виртуальное окружение:
```
python3 -m venv .venv
```

Активируем виртуальное окружение:

```
source .venv/bin/activate
```

Далее устанавливаем все из файла requirements.txt

```
Django==4.2.2
django-seed==0.3.1
psycopg2==2.9.6
psycopg2-binary==2.9.6
```

Для этого можно использовать команду
```
python -m pip install <name_packages>
```

Теперь нужно зайти в папку где лежит manage.py
```
cd pet_blog_project
```

Делаем миграции
```
python manage.py migrate
```

Генерируем данные
```
python manage.py seed articles --number=5
```

Что бы запустить сервер, для этого нужно перейти в папку с файлом manage.py и ввести команду:
```
python manage.py runserver
```