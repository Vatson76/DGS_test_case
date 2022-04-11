from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.db import migrations
from main.settings.base import TIME_ZONE


def add_task(apps, schema_editor):
    PeriodicTask.objects.create(
        name='Импорт логов Apache',
        task='apache_logs.tasks.parse_apache_logs',
        crontab=CrontabSchedule.objects.get_or_create(
            minute='0',
            hour='*',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
            timezone=TIME_ZONE
        )[0],
    )


class Migration(migrations.Migration):

    dependencies = [
        ('apache_logs', '0002_alter_apachelog_options'),
    ]

    operations = [
        migrations.RunPython(
            add_task,
            reverse_code=migrations.RunPython.noop
        )
    ]
