# veltrix_core/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "veltrix_core.settings")

app = Celery("veltrix_core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()