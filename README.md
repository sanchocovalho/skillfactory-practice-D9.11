# Задание D9.11

   Проект миниблога на Django

Для того, чтобы запустить локальный сервер необходимо:
1) Распакуйте проект в папку C:\my_site
2) Откройте командную строку и зайдите в директорию проекта:
   - cd C:\my_site
3) Создате виртуальное окружение:
   - python -m venv django
4) Активируйте виртуальное окружение:
   - django\Scripts\activate.bat
5) Установите все необходимые пакеты:
   - pip install -r requirements.txt
6) Выполнить следующий команды:
   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py createsuperuser
   - python manage.py runserver

Для того, чтобы сделать деплой на heroku необходимо:
1) Перейти в каталог с проектом:
   - cd C:\my_site
2) Выпонить следующий команды:
   - git init
   - git add .
   - git commit -m "initial commit"
   - heroku login
   - heroku create
   - heroku addons:create heroku-postgresql --as DATABASE
   - heroku config:set SECRET_KEY=Ваш_секретный_код
   - git push heroku master
   - heroku run python manage.py migrate
   - heroku run python manage.py createsuperuser
3) Если необходимо переименовываем приложение:
   - heroku rename -a oldname newname
4) Запускаем приложение:
   - heroku open

   Данный проект находится на https://miniblog-skillfactory.herokuapp.com/
   По умолчанию логин и пароль для пользователя-администратора в проекте:
   Логин: pws_admin
   Пароль: sf_password
