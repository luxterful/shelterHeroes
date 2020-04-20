startserver:
	python manage.py runserver

startclient:
	cd ./ShelterHeroesClient && yarn start

install:
	pip install -r requirements.txt
	cd ./ShelterHeroesClient && yarn install 

init_repo:
	python manage.py makemigrations users
	python manage.py makemigrations core
	python manage.py migrate
	python manage.py init_demo_db --flush