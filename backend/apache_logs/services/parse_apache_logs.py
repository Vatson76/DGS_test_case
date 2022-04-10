import re
from datetime import datetime


def parse_line(line: str) -> re.Match | None:
    regex = '(?P<ip>([\d\.]+:\d+)|(::1)) - - \[(?P<date>.*?)] "(?P<request>.*?)" (?P<status_code>\d+)'
    return re.search(regex, line)


def parse_date(date_line: str) -> datetime:
    return datetime.strptime(date_line, '%d/%b/%Y:%H:%M:%S %z')


def parse_request(request_line: str) -> re.Match | None:
    regex = '(?P<request_type>.+) (?P<uri>\/.+|\/*) (?P<protocol>.+)'
    return re.search(regex, request_line)
