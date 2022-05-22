# DRF(Django REST framework) - Email Login with Password(and hashing), Bearer with JWT Token, ORM with MySQL

## Install

```shell
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install django==3.2.12
$ pip install djangorestframework==3.12.4
```
Set up a new project with a single application
```shell
$ django-admin startproject project . 
$ django-admin startapp app
```

## Migration
```shell
$ python manage.py migrate
```

## Create admin user
Please input admin's password.
```shell
$ python manage.py createsuperuser --email admin@taptorestart.com --username admin
Password: verysecret
Password (again): verysecret
```

## Run
```shell
$ python manage.py runserver
```
