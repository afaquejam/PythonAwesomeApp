all:
	./awesome_app
clean:
	-find . -name "*.log" -delete
	-find . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
