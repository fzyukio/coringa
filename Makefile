

default:
	docker-compose up

build:
	docker-compose build

console:
	docker-compose run django bash

migrate:
	docker-compose run django python3 manage.py migrate

createsuperuser:
	docker-compose run django python3 manage.py createsuperuser

shell:
	docker-compose run django python3 manage.py shell

dbshell:
	docker-compose run postgres psql -d postgres

test:
	docker-compose run django python3 manage.py test
