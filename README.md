Установка и Настройка
=====================
Обратите внимание на пункт 3 в разделе Apache
- **Python**
1. Установить python 3.10
2. Создать виртуальное окружение `python -m venv`
3. Установить необходимые библиотеки выполнив `pip install -r requirements.txt`

- **Apache**.

   **Данное [видео](https://www.youtube.com/watch?v=frEjX1DNSpc&t=1173s) может помочь в разворачивании Apache**

1. Скачать и установить Apache 2.4 по пути **C:/Apache24**. Или другое удобное расположение
Например [отсюда](https://www.apachelounge.com/download/).
2. Открыть терминал CMD с правами администратора. Перейти в папку, куда установили Apache **(например
C:/Apache24)** с помощью cd и выполнить команду
`bin\httpd.exe -k install` для установки сервисов Apache. Запуск сервиса `bin/httpd.exe -k start`
Чтобы проверить успешную установку перейдите по адресу 
localhost на котором, в случае успешной установки, появится тестовая страница
3. Установите Microsoft C++ Build Tools. Это необходимо сделать перед выполнением pip install mod_wsgi.
4. В терминале выполнить  `mod_wsgi-express module-config`, скопировать полученный контекст в файл 
apache.conf на место соответствующих строк. Затем изменить пути до проекта в данном файле.
5. В терминале выполнить `/bin/httpd.exe -k start` чтобы запустить сервис. Перейдя по адресу localhost
должна появиться страница index.html



- **Базы данных**
Для работы проекта потребуются следующие базы данных:
1. PostgreSQL
2. Redis

   Установить их локально на ПК или развернуть в docker контейнерах


- **Переменные окружения**

   Переменные окружения хранятся в файле **.env**, расположенному по пути **backend/main/settings**.
   Поля данного файла выглядят следующим образом

```text
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=db_name

SECRET_KEY=**********************

LOG_FILE_PATH=path_to_file
LOG_FILE_NAME=file_name
BROKER_URL=broker_url
DEBUG= 1 or 2
```


Инструкции по эксплуатации
==========================
В проекте реализованы регистрация и авторизация пользователей на главной странице. С помощью которых можно получить 
логи обращения к собственным точкам проекта

За импорт логов отвечает команда **parse_apache_logs** расположенная в **backend/apache_logs/management/commands**
Для удобства, там же лежит уже готовый файл логов, на котором можно провести проверку работоспосоности команды

Также на проекте запущена celery таска, работающая каждый час, для импорта логов по указанному пути + маске файла

Для проверки работы сервисов написаны юнит-тесты, которые можно запустить командой python manage.py test

Для получения данных из БД можно прибегнуть к следующим способам: 
1. Через админку

   Для доступа к админке необходимо создать супер пользователя `python manage.py createsuperuser`
Таким образом вы получите данные к пользователям и импортированным в БД логам. 

2. Через документацию swagger
   
   Также данные из БД о логах можно получить с помощью страницы документации swagger по адресу **/swagger**

3. Через запрос к API точке

   Также данные из БД о логах можно получить через **postman** обращаюсь к точке **api/v1/apache_logs**

