all:
	./awesome_app
test:
	python -m pytest
clean:
	-find . -name "*.log" -delete
	-find . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
