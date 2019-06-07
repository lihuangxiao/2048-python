init:
	virtualenv -p python3 venv; . venv/bin/activate; pip install --upgrade -r requirements.txt
test:
	. venv/bin/activate; export PYTHONPATH='.'; pytest
