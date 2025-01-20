SOURCE_DIR = src
TEST_DIR = tests
PROJECT_DIRS = $(SOURCE_DIR) $(TEST_DIR)
PWD := $(dir $(abspath $(firstword $(MAKEFILE_LIST))))
PROJECT_VERSION ?= $(shell poetry version -s)
PROJECT_NAME ?= $(shell poetry version | cut -d' ' -f1)
PYTHON_VERSION ?= $(shell cat .python-version)

## Target convention naming:
## <Action>[-<Identifier>] :: Examples:
### `install` -> Just the action because is a generic task may implies other tasks.
### `install-poetry` -> The action first, the name after.
### `build-docker` -> Action and identifier.
### `rm-build-docker` -> Action taken for a action result.
## Why?
### Because helps to find the correct targets using the Shell AutoCompletion.

.PHONY: install install-poetry install-pre-commit
install: install-poetry install-pre-commit

install-poetry:
	poetry install --no-root

install-pre-commit:
	poetry run pre-commit install

.PHONY: build-docker
build-docker:
	docker build -t "${PROJECT_NAME}:latest" -t "${PROJECT_NAME}:${PROJECT_VERSION}" "${PWD}"

.PHONY: rm-build-docker
rm-build-docker:
	docker image rm "${PROJECT_NAME}" "${PROJECT_NAME}:${PROJECT_VERSION}"

.PHONY: clean
clean:
	find "${PWD}${SOURCE_DIR}/" -name "__pycache__" -type d -exec rm -rfv {} +
	find "${PWD}${TEST_DIR}/" -name "__pycache__" -type d -exec rm -rfv {} +

.PHONY: test
test:
	poetry run pytest --cov=$(SOURCE_DIR) -s --capture=no --log-cli-level=0 $(TEST_DIR)

.PHONY: pre-commit lint
lint: pre-commit
pre-commit:
	poetry run pre-commit run --all-files

.PHONY: info
info:
	@echo "${PROJECT_NAME};${PROJECT_VERSION};${PYTHON_VERSION}"

.PHONY: info-name
info-name:
	@echo "${PROJECT_NAME}"

.PHONY: info-version
info-version:
	@echo "${PROJECT_VERSION}"

.PHONY: serve
serve:
	poetry run uvicorn --host=0.0.0.0 --port=8000 --reload 'src.app.instances.api:api'
