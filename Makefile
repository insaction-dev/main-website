make:
	pipenv install && pipenv install --dev
	pipenv run make configure

configure:
	python manage.py makemigrations blog website
	python manage.py migrate
	python manage.py collectstatic --no-input
	python manage.py loaddata data/fixtures.json

server:
	pipenv run env DJANGO_SETTINGS_MODULE=insaction.settings.dev gunicorn -w 4 --access-logfile insaction.wsgi:application

production:
	pipenv run env DJANGO_SETTINGS_MODULE=insaction.settings.prod gunicorn -w 4 insaction.wsgi:application

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