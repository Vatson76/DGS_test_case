from django.conf.urls import include, url
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apache_logs.urls import urlpatterns as apachelog_urlpatterns


openapi_info = openapi.Info(
      title="API для логов",
      default_version='beta',
      description='АПИ для получения логов из базы данных',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="vadim.gartman@yandex.u"),
      license=openapi.License(name="BSD License"),
   )

schema_view = get_schema_view(
    openapi_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        url('api/v1/', include(apachelog_urlpatterns)),
    ]
)

