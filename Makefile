startserver:
	python manage.py runserver

startclient:
	cd ./ShelterHeroesClient && yarn start

install:
	pip install -r requirements.txt
	cd ./ShelterHeroesClient && yarn install 

init_repo:
	python manage.py makemigrations users
	python manage.py makemigrations storage
	python manage.py makemigrations core
	python manage.py migrate

reset_repo:
	find ShelterHeroesServer -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find ShelterHeroesServer -path "*/migrations/*.pyc" -delete