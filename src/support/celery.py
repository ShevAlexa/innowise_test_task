from __future__ import absolute_import
from celery import Celery
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support.settings')

app = Celery('support', broker='redis://cache:6379/1')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
