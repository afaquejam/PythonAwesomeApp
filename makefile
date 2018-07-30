all:
	./awesome_app

test:
	python -m pytest

test_report:
	mkdir -p reports
	python3 -m pytest --cov-config .coveragerc --cov-report html:reports/package_one --cov=package_one
	python3 -m pytest --cov-config .coveragerc --cov-report html:reports/package_two --cov=package_two
	-firefox reports/package_one/index.html reports/package_two/index.html &

freeze-dependencies:
	pip3 freeze > requirements.txt

upgrade-dependencies:
	pip3 install -r requirements-to-freeze.txt --upgrade

clean:
	-find . -name "*.log" -delete
	-find . -name "*.dat" -delete
	-find . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
	-rm -rf .pytest_cache
	-rm -rf reports
	-rm -rf awesome_app.spec app.prof build dist

hard-clean: clean
	-rm -rf virtualenv
