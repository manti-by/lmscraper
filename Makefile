venv:
	virtualenv -p $(shell which python3) --no-site-packages --prompt='lms-' ../venv

pip:
	pip install -Ur requirements.txt

check:
	black -t py36 ./
	isort
	flake8
