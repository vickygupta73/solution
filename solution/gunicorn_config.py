# gunicorn_config.py

bind = "0.0.0.0:8000"
workers = 4
chdir = "/Users/mac/project/solution"
module = "solution.wsgi:application"


