from django.contrib import admin
from .models import ApacheLog


@admin.register(ApacheLog)
class ApacheLogAdmin(admin.ModelAdmin):
    #TODO написать фильтры
    pass
