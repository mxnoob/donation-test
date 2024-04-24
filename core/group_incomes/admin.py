from django.contrib import admin

from .models import Collect, Payment

admin.site.register(Payment)


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
