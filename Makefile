.PHONY: helpt init start testapp lint test test-coverage test-ci clean-pyc publish update-test-fixture
.DEFAULT_GOAL := help

help: ## See what commands are available.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36mmake %-15s\033[0m # %s\n", $$1, $$2}'

init: clean-pyc ## Install dependencies and initialise for development.
	pip install -e .[testing,docs] -U
	python ./tests/testapp/manage.py migrate
	python ./tests/testapp/manage.py loaddata test_data

start: ## Starts the development server.
	python ./tests/testapp/manage.py runserver

lint: ## Lint the project.
	pre-commit run --all-files

test: ## Test the project.
	python ./runtests.py

test-future: ## Test against trunk versions of dependencies to check for future compatibility.
	tox -e future

test-coverage: ## Run the tests while generating test coverage data.
	coverage run ./runtests.py && coverage report && coverage html

test-ci: ## Continuous integration test suite.
	tox

update-test-fixture: ## Update test fixture from the db.
	python ./tests/testapp/manage.py dumpdata --natural-foreign --indent 2 -e auth.permission -e contenttypes -e wagtailcore.GroupCollectionPermission -e wagtailimages.rendition -e sessions -e wagtailcore.referenceindex -e wagtailcore.pagesubscription -e wagtailcore.workflowcontenttype -e wagtailadmin.editingsession > tests/testapp/home/fixtures/test_data.json

clean-pyc: ## Remove Python file artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
