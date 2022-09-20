from django.contrib import admin

from landingpage.models import *


@admin.register(Result)
class BaseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Result._meta.get_fields()]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.get_fields()]