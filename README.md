# Задание D9.11

   Проект миниблога на Django

  ТехЗадание:
  Для более удобного поиска сделаем так, чтобы посты могли быть разбиты по категориям. Что для этого нужно сделать?
  - Добавить модель "Category". Установить отношение между моделями "Post" и "Category". Для простоты лучше исходить из того, что к посту может относиться только одна категория, но к одной категории может относиться множество постов.
  - Категория должна быть необязательным параметром поста. При удалении категории у всех связанных постов категория должна становиться равной null, то есть обнуляться.
  - Добавить категории в API, то есть создать обработчики и сериализаторы (полезно будет освежить память о вложенных связях в DRF).
  - Маршруты вашего приложения должны быть связаны с обработчиками списка категорий и единичной категорией: https://YOUR_HOST/categories/ и https://YOUR_HOST/categories/<int:pk> соответственно.
  - При этом на запрос GET по адресу https://YOUR_HOST/categories/ сервер должен отвечать списком всех категорий и входящих в них постов. По запросу POST на этот адрес должна создаваться новая категория, а информация о ней должна возвращаться в качестве ответа сервера с HTTP статусом 201 (created).
  - На запрос GET по адресу https://YOUR_HOST/categories/<int:pk> сервер должен отображать информацию только об одной категории, id которой был передан в запросе.

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
   - heroku config:set DISABLE_COLLECTSTATIC=1 (опционально)
   - git push heroku master
   - heroku config:unset DISABLE_COLLECTSTATIC (опционально)
   - heroku run python manage.py collectstatic --noinput (опционально)
   - heroku run python manage.py makemigrations
   - heroku run python manage.py migrate
   - heroku run python manage.py createsuperuser
3) Если необходимо переименовываем приложение:
   - heroku rename -a oldname newname
4) Запускаем приложение:
   - heroku open

   Данный проект находится на https://miniblog-skillfactory.herokuapp.com/
   По умолчанию логин и пароль для пользователя-администратора в проекте:
   - Логин: pws_admin
   - Пароль: sf_password
