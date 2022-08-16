from django.contrib import admin

from landingpage.models import Result


@admin.register(Result)
class BaseAdmin(admin.ModelAdmin):
    pass
