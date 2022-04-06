from .base import TIME_ZONE
from multiprocessing import cpu_count

CELERY_ENABLED = True
CELERY_TIMEZONE = TIME_ZONE

CELERY = {
    'broker_url': 'redis://redis:6379/1',
    'enable_utc': False,
    'timezone': TIME_ZONE,
    'accept_content': ['json'],
    'task_serializer': 'json',
    'result_serializer': 'json',
    'worker_disable_rate_limits': False,
    'worker_pool_restarts': True,
    'worker_concurrency': cpu_count(),
    'result_backend': 'redis://redis:6379/1',
    'task_ignore_result': False,
    'result_extended': True,
    'result_expires': 60 * 60 * 4,
    #'beat_scheduler': 'django_celery_beat.schedulers:DatabaseScheduler',
}
