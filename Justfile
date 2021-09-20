build:
	@poetry build

test:
	@poetry run pytest

format:
	@black -l 79 **/*.py
