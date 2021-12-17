setup_python_env:
	pip install virtualenv
	rm -rf venv
	python3 -m virtualenv venv
	chmod 755 venv/bin/activate
	venv/bin/activate
	pip install -r requirements.txt

start:
	docker-compose up -d

stop:
	docker-compose down

rebuild:
	docker-compose down
	docker-compose up -d --build

restart:
	docker-compose restart

shell:
	docker-compose exec web bash

makemigrations: start
	docker-compose exec web ./manage.py makemigrations

migrate: start
	docker-compose exec web ./manage.py migrate

test: start
	docker-compose exec web ./manage.py test

loaddata: start
	docker-compose exec web ./manage.py loaddata user/fixtures/* || true

logs:
	docker-compose logs -f web

dummy_data: start
	docker-compose exec web ./manage.py dumpdata user auth.user --indent 4 > user/fixtures/dummy_data.json || true

