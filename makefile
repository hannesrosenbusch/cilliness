install:
	pip install -r requirements.txt

lint:
	pylint --generated-members="torch.*" maximize.py

test:
	python3 -m pytest -vv -cov=maximum test_maximize.py