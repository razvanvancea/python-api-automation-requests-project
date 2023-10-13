prerequisite: python3, pip

setup:
pip install faker
pip install requests
pip install pytest

run tests:
pytest -v
python3 test_users_api.py
python3 -m pytest -v 
