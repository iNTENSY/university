# Проект: Контроль посещаемости обучающихся в образовательном учреждении

Данный проект является выпускной квалифицированной работой
для университета. 

Цель данной работы заключается в контроле
посещении студентов, комфортный интерфейс для администраторов
и возможность сбора/отправки сведений за определенный отрезок
времени.

В проекте также реализован код для макета пропускной системы
написанной под Arduino (sketch.txt). Python-скрипт считывает данные 
работы макета с указанного порта и парсит полученные данные для
идентификации номера карточки, а после же отправляет эти данные
на существующий endpoint веб-сервиса.

### Технологический стек:
___

- Язык программирования: Python
- База данных: PostgreSQL
- Веб-фреймворк: Django
- Драйвер для PostgreSQL: Psycopg2
