# Групповой сбор средств

Этот репозиторий содержит приложение Django, предназначенное для управления групповыми мероприятиями по сбору средств.
Приложение позволяет пользователям эффективно создавать, управлять и участвовать в мероприятиях по сбору средств. Ниже
вы найдете инструкции по настройке и запуску проекта.

## Стек технологий

<p align="center">
    <a href="https://www.djangoproject.com/">
        <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white">
    </a>
    <a href="https://www.django-rest-framework.org/">
        <img alt="Django-REST-Framework" src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray">
    </a>
    <a href="https://www.postgresql.org/">
        <img alt="PostgreSQL" src="https://img.shields.io/badge/postgresql-%23336791.svg?&style=for-the-badge&logo=postgresql&logoColor=white">
    </a>
    <a href="https://docs.celeryq.dev/en/stable/">
        <img alt="PostgreSQL" src="https://img.shields.io/badge/celery-%2337814A.svg?&style=for-the-badge&logo=celery&logoColor=white">
    </a>
    <a href="https://redis.io">
        <img alt="PostgreSQL" src="https://img.shields.io/badge/redis-%23DC382D.svg?&style=for-the-badge&logo=redis&logoColor=white">
    </a>
    <a href="https://nginx.org/ru/">
        <img alt="Nginx" src="https://img.shields.io/badge/nginx-%23269539.svg?&style=for-the-badge&logo=nginx&logoColor=white">
    </a>
    <a href="https://gunicorn.org/">
        <img alt="gunicorn" src="https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white">
    </a>
    <a href="https://www.docker.com/">
        <img alt="docker" src="https://img.shields.io/badge/docker-%232496ED.svg?&style=for-the-badge&logo=docker&logoColor=white">
    </a></br></br>
    <a href="Тестовое%20задание%20Backend%20Python.pdf">
        <img alt="docker" src="https://img.shields.io/badge/Тестовое_задание-494788?style=for-the-badge">
    </a>
</p>

## Функции

- Регистрация и аутентификация пользователя
- Создавайте и управляйте мероприятиями по сбору средств
- Отслеживание целей и обновления прогресса
- Система уведомлений при создании сбора или доната

## Запуск

```shell
# Склонировать репозиторий
git clone git@github.com:mxnoob/donation-test.git
```

> [!IMPORTANT]
> Необходимо создать файл `.env` с переменными окружения.</br>
> Пример файла [.env.example](.env.example)

```shell
# Запустить докер композ
docker compose up -d --build
```