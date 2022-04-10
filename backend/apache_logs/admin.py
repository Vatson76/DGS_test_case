from django.contrib import admin
from .models import ApacheLog
from .filters.admin_filters import IpFilter
from rangefilter.filters import DateRangeFilter


@admin.register(ApacheLog)
class ApacheLogAdmin(admin.ModelAdmin):
    list_display = ('ip', 'request_type', 'uri', 'date')
    search_fields = ('ip',)

    date_hierarchy = 'date'

    list_filter = (
        IpFilter,
        ('date', DateRangeFilter),
        'request_type',

    )
