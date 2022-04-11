from main.celery import app
from django.core.management import call_command


@app.task
def parse_apache_logs(*args, **kwargs):
    call_command('parse_apache_logs', verbosity=0)
