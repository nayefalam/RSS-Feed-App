from celery.schedules import crontab
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

app.conf.beat_schedule = {
    'fetch-feeds-every-10-minutes': {
        'task': 'tasks.run_app',
        'schedule': crontab(minute='*/10'),  # Every 10 minutes
    },
}
