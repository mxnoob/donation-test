from django.contrib import admin

from .models import Collect


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
