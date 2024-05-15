from django.core.cache import cache
from django.db.models import signals
from django.dispatch import receiver

from group_incomes.models import Collect, Payment
from group_incomes.services import (
    success_created_collect_email,
    success_created_payment_email,
)


@receiver(signals.post_save, sender=Payment)
def update_payment(sender, instance, created, **kwargs):
    dispose_collect(instance.collect.id)
    if created:
        success_created_payment_email(instance.author.email)


@receiver(signals.post_save, sender=Collect)
def update_collect(sender, instance, created, **kwargs):
    dispose_collect(instance.id)
    if created:
        success_created_collect_email(instance.author.email)


def dispose_collect(collect_id):
    cache.delete('collects')
    cache.delete('collect:%s' % collect_id)
