.PHONY: project

project:
	django-admin startproject $(PROJECT_NAME)

.PHONY:runserver

runserver:
	python3 MVT_Architecture_Python/manage.py runserver

.PHONY: startapp

startapp:
	python3 MVT_Architecture_Python/manage.py startapp $(APP_NAME)