import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bright_money_plaid_assignment.settings')

app = Celery('Bright_money_plaid_assignment')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()