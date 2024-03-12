POETRY := $(shell command -v poetry 2> /dev/null)

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

.PHONY: poetry_installed
poetry_installed:
ifndef POETRY
	@echo "Poetry does not seem to be installed, but it's required."
	@echo "You can install it by typing: make install_poetry"
	@echo "For more details about how you can install poetry, see https://python-poetry.org/"
	@exit 1
endif

.PHONY: install_poetry
install_poetry:  ## Install poetry
ifndef POETRY
	curl -sSL https://install.python-poetry.org | python3 -
endif

.PHONY: dev
dev: poetry_installed  ## Setup the development environment
	poetry --version
	poetry run python --version
	poetry check || poetry update
	poetry install --all-extras
	poetry env info
	poetry show

.PHONY: test
test: poetry_installed  ## Run the tests
	poetry run coverage run -m pytest
#	poetry run coverage run --source=. -m unittest discover -s tests -v
	poetry run coverage report

.PHONY: format
format: poetry_installed  ## Format the code
	poetry run isort andz tests
	poetry run black andz tests

.PHONY: check_format
check_format: poetry_installed  ## Check if the code is formatted
	poetry run isort --check --diff andz tests
	poetry run black --check --diff andz tests

.PHONY: check_types
check_types: poetry_installed  ## Run type-checks
	poetry run mypy andz

.PHONY: check_style
check_style: poetry_installed  ## Run style checks
	poetry run pylint andz tests

.PHONY: check
check: check_format check_types check_style  ## Run all quality assurance checks
