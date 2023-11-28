# Тестовое задание в кампанию EasyWay

# Запуск проекта

### Поднять (сборка, создание, старт)
##### Сборка контейнеров
> ./dc build
##### Поднять все контейнеры в фоне
> ./dc up -d
##### Поднять все контейнеры со сборкой
> ./dc up --build
##### Создать суперпользователя
> docker exec -it django_app ./manage.py createsuperuser
##### Создать данные для теста
> docker exec -it django_app ./manage.py create_dummy_data

## [Ссылка на тестовое задание](https://bitbucket.org/stssokolsts/docs/src/master/test_app/)

