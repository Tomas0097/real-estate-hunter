.DEFAULT_GOAL := default
SHELL := /bin/bash

manage_command = docker exec -it real-estate-hunter-app /manage.sh


default:
	@echo "Please specify target. Check contents of Makefile to see list of available targets."

prepare_database:
	docker exec -it real-estate-hunter-db /real_estate_hunter-init.sh

makemigrations:
	$(manage_command) makemigrations -n '_' $(options) web

makemigrations_data:
	$(manage_command) makemigrations -n '_' --empty web

migrate:
	$(manage_command) migrate $(app) $(migration)

app_bash:
	docker exec -it real-estate-hunter-app bash

test:
	$(manage_command) test

shell:
	$(manage_command) shell

manage:
	$(manage_command) $(command)

start_app:
	docker-compose up -d

up: start_app

down:
	docker-compose down

pull:
	docker-compose pull
