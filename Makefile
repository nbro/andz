POETRY := $(bash command -v poetry 2> /dev/null)

.PHONY: poetry_check
poetry_check:
ifndef POETRY
	@echo "Poetry does not seem to be installed, but it's required. Please, install it. See https://python-poetry.org/"
	@exit 1
endif

.PHONY: ensure_poetry
ensure_poetry:
ifndef POETRY
	curl -sSL https://install.python-poetry.org | python3 -
endif

.PHONE: format
format: ensure_poetry  ## Format all code inside ands and tests with isort and black
	poetry run isort ands tests
	poetry run black ands tests

.PHONE: check_format
check_format: ensure_poetry  ## Check if the code inside ands and tests is formatted correctly according to isort and black
	poetry run isort --check ands tests
	poetry run black --check ands tests

.PHONY: test
test: ensure_poetry  ## Run all the tests
#	poetry run coverage run -m pytest
	poetry run coverage run --source=. -m unittest discover -s tests -v
	poetry run coverage report

.PHONY: check_types
check_types: ensure_poetry  ## Run type-checks with mypy
	poetry run mypy ands

.PHONY: check_style
check_style: ensure_poetry  ## Run style checks with PyLint
	poetry run pylint ands

.PHONY: quality
quality: check_format check_types check_style test  ## Run all quality assurance checks (format checks, type-checks, style checks and the tests)

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-30s\033[0m %s\n", $$1, $$2}'
