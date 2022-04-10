from rest_framework import routers
from .views import ApacheLogViewSet

router = routers.DefaultRouter()
router.register(r'apache_logs', ApacheLogViewSet, basename='apache-logs')

urlpatterns = router.urls
