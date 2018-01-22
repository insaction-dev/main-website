make:
	pipenv install && pipenv install --dev
	pipenv run make configure

configure:
	python manage.py makemigrations blog website
	python manage.py migrate
	python manage.py collectstatic --no-input
	python manage.py loaddata data/fixtures.json

server:
	pipenv run env DJANGO_SETTINGS_MODULE=insaction.settings.dev ./manage.py runserver 0.0.0.0:8000

production:
	pipenv run gunicorn --env DJANGO_SETTINGS_MODULE=insaction.settings.prod --config gunicorn.py insaction.wsgi:application

tests:
	pipenv run python manage.py test blog website

coverage:
	pipenv run coverage run --source='.' manage.py test
	
cov-xml:
	pipenv run coverage xml

cov-html:
	pipenv run coverage html

cov-codacy: cov-xml
	pipenv run python-codacy-coverage -r coverage.xml