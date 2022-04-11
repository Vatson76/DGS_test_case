from django.test import SimpleTestCase
from .services.parse_apache_logs import (
    parse_line,
    parse_date,
    parse_request
)
from datetime import datetime, timezone, timedelta


class ServicesTestCase(SimpleTestCase):
    def test_parse_line(self):
        test_line = '::1 - - [10/Apr/2022:15:18:23 +0300] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380'
        result = parse_line(test_line)
        #self.assertIsNotNone(result)
        self.assertEqual(result['ip'], '::1')
        self.assertEqual(result['date'], '10/Apr/2022:15:18:23 +0300')
        self.assertEqual(result['request'], 'GET /static/admin/css/dashboard.css HTTP/1.1')
        self.assertEqual(result['status_code'], '200')

    def test_parse_request(self):
        test_line = 'GET /static/admin/css/dashboard.css HTTP/1.1'
        result = parse_request(test_line)
        #self.assertIsNotNone(result)
        self.assertEqual(result['request_type'], 'GET')
        self.assertEqual(result['uri'], '/static/admin/css/dashboard.css')
        self.assertEqual(result['protocol'], 'HTTP/1.1')

    def test_parse_date(self):
        test_line = '10/Apr/2022:15:18:23 +0300'
        result = parse_date(test_line)
        tz = timezone(timedelta(hours=3))

        right_datetime = datetime(2022, 4, 10, 15, 18, 23, tzinfo=tz)
        self.assertEqual(result, right_datetime)
