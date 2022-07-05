build: #run build package
	poetry build

package-install: #install package
	python3 -m pip uninstall dist/*.whl
	python3 -m pip install --user dist/*.whl

lint: #linter for code
	poetry run flake8 page_loader tests

test-package: #test package without install
	poetry run python3 -m page_loader.scripts.script_page_loader

test: #start pytest
	poetry run pytest -vv

coverage: #start pytest code coverage
	poetry run pytest --cov page_loader

coverage-xml: #start pytest code coverage and write report is xml-file
	poetry run pytest --cov page_loader --cov-report xml

