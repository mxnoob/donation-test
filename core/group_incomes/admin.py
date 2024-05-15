from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Collect, Event, Payment

admin.site.register(Event)
admin.site.register(Payment)


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.unregister(Group)
