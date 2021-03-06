from django.db import models


class RequestTypes(models.TextChoices):
    GET = 'GET', 'GET'
    HEAD = 'HEAD', 'HEAD'
    POST = 'POST', 'POST'
    PUT = 'PUT', 'PUT'
    DELETE = 'DELETE', 'DELETE'
    CONNECT = 'CONNECT', 'CONNECT'
    OPTIONS = 'OPTIONS', 'OPTIONS'
    TRACE = 'TRACE', 'TRACE'
    PATCH = 'PATCH', 'PATCH'


class ApacheLog(models.Model):
    ip = models.CharField(
        blank=False,
        null=False,
        max_length=128,
        verbose_name='ip пользователя'
    )
    date = models.DateTimeField(null=False, blank=False)
    request = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Запрос'
    )
    request_type = models.CharField(
        choices=RequestTypes.choices,
        verbose_name='Тип запроса',
        max_length=20
    )
    uri = models.CharField(
        null=False,
        blank=False,
        max_length=128,
        verbose_name='URI запроса'
    )
    protocol = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        verbose_name='Протокол',
    )
    status_code = models.SmallIntegerField(
        verbose_name='Код статуса'
    )

    class Meta:
        ordering = '-date',
        verbose_name = 'Лог Apache'
        verbose_name_plural = 'Логи Apache'

    def __str__(self):
        return 'Лог ip {ip}, тип запроса {request_type}'.format(
            ip=self.ip,
            request_type=self.request_type
        )
