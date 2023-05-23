.PHONY: project

project:
	django-admin startproject $(PROJECT_NAME)

.PHONY:runserver

run:
	python3 manage.py runserver $(PORT)

.PHONY: startapp

startapp:
	python3 manage.py startapp $(APP_NAME)


.PHONY: variables

PORT=8080
PROJECT_NAME=MVT_Architecture_Python
APP_NAME=""