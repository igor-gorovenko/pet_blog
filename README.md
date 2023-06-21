# Проект pet_blog

Скопируйте репозиторий
```
git clone git@github.com:igor-gorovenko/pet_blog.git
```

У вас должен быть установлен питон 3 версии, скачать можно тут: https://www.python.org/

Создаем виртуальное окружение:
```
python3 -m venv venv
```

Активируем виртуальное окружение:

```
source ./venv/bin/activate
```

Далее устанавливаем все с файла requirements.txt

```
Django==4.2.2
django-seed==0.3.1
```

Для этого можно использовать команду
```
python -m pip install <name_source>
```

Что бы запустить проект, для этого нужно перейти в папку с файлом manage.py и ввести команду:
```
python manage.py runserver
```

У вас должен запустить сервер.
Переходим на url и в браузере вы дожны видеть что то подобное:

Превью проекта
<img width="1014" alt="Screenshot 2023-06-19 at 15 22 20" src="https://github.com/igor-gorovenko/pet_blog/assets/59226858/79c90f79-a4b3-4a70-b8ad-04e84fb3f4f7">
