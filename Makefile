make:
	pipenv install && pipenv install --dev
	pipenv run make configure

configure:
	python manage.py makemigrations blog website
	python manage.py migrate
	python manage.py collectstatic --no-input
	python manage.py loaddata data/fixtures.json

server:
	pipenv run python manage.py runserver

tests:
	pipenv run python manage.py test blog website

coverage:
	-pipenv run coverage run --source='.' manage.py test
	pipenv run coverage xml

cov-html:
	pipenv run coverage html

cov-upload:
	pipenv run python-codacy-coverage -r coverage.xml