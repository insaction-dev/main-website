.PHONY: server production

make:
	pipenv install --dev
	DJANGO_SETTINGS_MODULE=insaction.settings.dev pipenv run make configure

configure: now.json
	./manage.py makemigrations blog mgmt website
	./manage.py migrate
	./manage.py collectstatic --no-input
	touch now.json

bootstrap: configure
	./manage.py loaddata data/fixtures.json

server:
    DJANGO_SETTINGS_MODULE=insaction.settings.dev make bootstrap
	DJANGO_SETTINGS_MODULE=insaction.settings.dev ./manage.py runserver 0.0.0.0:8000

production: configure
	gunicorn --config gunicorn.py insaction.wsgi:application

tests:
	pipenv run ./manage.py test blog website

coverage:
	pipenv run coverage run --source='.' manage.py test
	
cov-xml:
	pipenv run coverage xml

cov-html:
	pipenv run coverage html

cov-codacy: cov-xml
	pipenv run python-codacy-coverage -r coverage.xml