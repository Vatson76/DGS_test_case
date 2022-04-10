from apache_logs.models import ApacheLog
from apache_logs.services.parse_apache_logs import (
    parse_date,
    parse_line,
    parse_request
)
from django.core.management.base import BaseCommand
from decouple import config


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = config('LOG_FILE_PATH') + config('LOG_FILE_NAME')
        with open(file_path, 'r') as log_file:
            for line in log_file:
                parsed_line = parse_line(line)
                date = parse_date(parsed_line['date'])
                parsed_request = parse_request(parsed_line['request'])
                try:
                    ApacheLog.objects.update_or_create(
                        date=date,
                        defaults={
                            'ip': parsed_line['ip'],
                            'request': parsed_line['request'],
                            'status_code': parsed_line['status_code'],
                            'request_type': parsed_request['request_type'],
                            'uri': parsed_request['uri'],
                            'protocol': parsed_request['protocol']
                        }
                    )
                except Exception:
                    pass

