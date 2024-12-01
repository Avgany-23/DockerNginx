# Создание контейнеров для поднятия Django проекта, использующий Nginx и PostgreSQL

#### &nbsp; &nbsp;Контейнеры поднимаются на хосте 192.168.0.110. Его нужно изменить на контейнер с хостом своего сервера.
<br>
Для замены хоста необходимо изменить хост на своей в этом файле или в файле startup.sh в корне проекта, если контейнеры
 запускаются через sh скрипт.

Также обязательно нужно изменить хост по пути nginx/project.conf в 3 и 6 строке (порт не менять).

- в результате будет создано 3 образа, 3 контейнера, 2 тома и 1 мостовая сеть.

### Первый вариант запуска: скрипт на автоматическое поднятие контейнеров
```
chmod +x startup.sh
sh startup.sh
```

### Второй вариант запуска: прописать всё самостоятельно из корня проекта
> **Важно**: все команды прописываются в том порядке, в каком они приведены ниже
#### Для сети bridge (мостовой):
```docker network create project_bridge```
- __Тома будут созданы автоматически при поднятии контейнеров__

#### Для Nginx:
```
docker build -f nginx/Dockerfile . -t nginx_image
docker run -d --name nginx_cont -p 80:80 --network project_bridge -v static_volume:/usr/src/app/static nginx_image
```

#### Для Базы Данных:
```
docker build -f db/Dockerfile . -t db_image
docker run -d --name db_cont -v data_volume:/var/lib/data_psql -p 5432:5432 --network project_bridge db_image
```

#### Для project Django:
```
docker build -f project/Dockerfile project -t project_image

docker run \
    --name project_cont \
    -v static_volume:/usr/src/app/static \
    -e DB_HOST=db_cont \
    -e PROJECT_HOST=192.168.0.110 \
    -p 8000:8000 \
    -d \
    --network project_bridge \
    project_image
```