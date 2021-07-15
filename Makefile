up: docker-up
down: docker-down
reset: down up
in: docker-inside
attach: docker-attach
hardreset: down docker-up-build

docker-up:
	docker-compose up -d devmanweb

docker-up-build:
	docker-compose up --build -d devmanweb

docker-down:
	docker-compose down -v --remove-orphans

docker-inside:
	docker exec -it devman_devmanweb_1 bash

docker-attach:
	docker attach devman_devmanweb_1