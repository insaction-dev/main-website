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