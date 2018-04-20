all:
	./awesome_app
test:
	python -m pytest
test_report:
	mkdir -p reports
	python3 -m pytest --cov-config .coveragerc --cov-report html:reports/package_one --cov=package_one
	python3 -m pytest --cov-config .coveragerc --cov-report html:reports/package_two --cov=package_two
	-firefox reports/package_one/index.html reports/package_two/index.html &
clean:
	-find . -name "*.log" -delete
	-find . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
	rm -rf reports
