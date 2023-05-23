.PHONY: project

project:
	django-admin startproject $(PROJECT_NAME)

.PHONY:runserver

runserver:
	python3 MVT_Architecture_Python/manage.py runserver

.PHONY: startapp

startapp:
	cd MVT_Architecture_Python && python3 manage.py startapp CRUD_App