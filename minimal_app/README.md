### Django 4.10, postgres:14.1, vue 3

### TODO
- [x] возможность автоматического развертывания по нажатию кпонки build
- [x] возможность отката проекта по хешу коммита на гитхабе и названию бекапа БД
- [x] бекап базы данных при каждом билде
- [ ] прогон тестов при каждом билде(например можем ли мы зарегаться, авторизоваться, создать пост и т.д.)
- [ ] поменять production сервер на django с python manage.py runserver на gunicorn
- [ ] каким-то образом сделать возможность деплоя на dev домены
- [ ] выполнять бекап базы данных переодически(например раз в неделю)
- [ ] вероятно вынести фронтенд и бекенд в отдельные репозитории
- [ ] настроить сжатие бакапа базы данных, включить параллельную его загрузку в базу
- [ ] сохранить текущие настройки jenkins as code
- [ ] запустить зеркало на gitea, чтобы не вышло как с deeppavlov
- [ ] научиться деплоить в cubernetes...

#### [Quickstart: Compose and Django](https://docs.docker.com/samples/django/)

```text
docker-compose run web django-admin startproject app .
```

- [development in django in docker container](https://youtu.be/ruIoLtqIdNc)
- [development in django in docker container - github repo](https://github.com/luabud/petgram/tree/main/.devcontainer)
- [enable django cors](https://www.stackhawk.com/blog/django-cors-guide/)
- [django apis book](https://github.com/wsvincent/restapiswithdjango)
- [django rest framework APIView](https://www.django-rest-framework.org/tutorial/3-class-based-views/)
- [django ultimate learning resourse](https://learndjango.com/)

### Backup your databases
```bash
docker-compose exec db pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```
```bash
docker-compose -f docker-compose.prod.yml exec db pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```

### запустить docker-compose из файла в фоне, с полным ребилдом
```bash
docker-compose -f docker-compose.prod.yml up --build -d
```

### Restore your databases
```bash
cat dump_01-09-2022_01_22_31.sql | docker-compose exec -T db psql -U postgres
```
```bash
cat dump_01-09-2022_01_22_31.sql | docker-compose -f docker-compose.prod.yml exec -T db psql --quiet -U postgres
```


### вывести теги в хронологическом порядке(по убыванию даты)
```bash
git tag -l --sort=-creatordate --format='%(refname:short)'
```

### вывести короткий хеш последнего коммита

```bash
git log -1 --pretty=format:'%h'
```

### вывести последний тег
```bash
git describe --tags --abbrev=0
```

### выполнить миграции в django
```bash
docker-compose run server python manage.py migrate
```

### начать конфигурацию s3
```bash
aws configure
```

### добавить aws credentials в jenkins
- [jenkins aws credentials](https://youtu.be/iiF2iQV-3eM)
- автогенерация кода для доступа к s3 в яндекс не работает, придется перепечатывать как на видео. но по итогу оно работает

### Подключение к хранилищу S3 в yandex через aws cli
- https://cloud.yandex.ru/docs/datasphere/operations/data/connect-to-s3
```text
AWS Access Key ID - это Идентификатор ключа
AWS Secret Access Key - это Ваш секретный ключ
Default region name [None] - это ru-central1, другой может не сработать
Default output format [None] - просто enter нажать
```

### Загрузить объект в s3
```bash
aws --endpoint-url=https://storage.yandexcloud.net/ s3 cp test-dump s3://postgre-backups/test-dump
```

aws --endpoint-url=https://storage.yandexcloud.net/ s3 cp dump_01-09-2022_01_22_31.sql s3://postgre-backups/dump_01-09-2022_01_22_31.sql

### скачать файл из yandex s3
```bash
aws --endpoint-url=https://storage.yandexcloud.net/ s3 cp s3://postgre-backups/v0.0.2__524af41__02-09-2022_13_47_15.sql v0.0.2__524af41__02-09-2022_13_47_15.sql
```

### Запушить тег на удаленный репозиторий
```bash
git push origin tag_name
```

### Ошибка с доступом к docker у jenkins
- Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version": dial unix /var/run/docker.sock: connect: permission denied
```bash
sudo usermod -a -G docker jenkins
reboot
```