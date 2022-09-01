### Django 4.10, postgres:14.1, vue 3

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

### Restore your databases
```bash
cat dump_01-09-2022_01_22_31.sql | docker-compose exec -T db psql -U postgres
```

### вывести теги в хронологическом порядке(по убыванию даты)
```bash
git tag -l --sort=-creatordate --format='%(refname:short)'
```