Run-server:
    - commands-run

    - python manage.py runserver

Start-Project-in-Django:
    - project commands

    - django-admin startproject project .

Start-app:
    - apps command

    - python manage.py startapp <appname>

DataBase:
    - database commands

    - python manage.py migrate
    - python manage.py makemigrations

Create-Super-user:
    - superuser command

    - python manage.py createsuperuser

Pillow installed for images

    - python -m pip install Pillow