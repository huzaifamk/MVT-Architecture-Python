.PHONY: project

project:
	django-admin startproject $(PROJECT_NAME)

.PHONY:runserver

run:
	python3 manage.py runserver

.PHONY: startapp

startapp:
	python3 manage.py startapp $(APP_NAME)