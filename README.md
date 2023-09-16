# API_book_exchange

**API Book Exchange** - это RESTful API для обмена, продажи и аренды книг между пользователями. Этот проект предоставляет разработчикам и пользователям возможность легко управлять книгами, оформлять заказы, оставлять отзывы и многое другое. В этом репозитории вы найдете всю необходимую информацию для работы с API Book Exchange.
## Введение

- Проект "Book Exchange" предоставляет множество возможностей для обмена и продажи книг, а также для нахождения интересных книг для чтения. Он разработан с использованием современных технологий и обеспечивает безопасность и удобство пользователей.

## Используемые технологии

- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) Django: Мощный веб-фреймворк на Python.
- ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) Django REST Framework: Библиотека для создания API на основе Django.
- ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) Swagger: Инструмент для создания интерактивной документации API.

---



## Лицензия

[![Лицензия](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

---

## Как начать
1) Клонировать репозиторий:
```
git clone https://github.com/zuhd-dev/API_book_exchange.git
```
2) Создайте виртуальное окружение: 
```
python -m venv .venv
```
3) Активируйте виртуальное окружение: 
```
.venv/bin/activate
```
4) Установите зависимости: 
```
pip install -r requirements.txt
```
5) Выполните миграции: 
```
python manage.py makemigrations
```
6) Примените миграции:
```
python manage.py migrate
```
7) Запустите сервер разработки: 
```
python manage.py runserver
```
Откройте админ-панель [localhost:8000/admin](http://localhost:8000/admin)

Логин администратора: husniddin

Пароль администратора: 1234

Откройте документацию API Swagger [localhost:8000/api/swagger/](http://localhost:8000/api/swagger/)