from django.core.cache import cache
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django_cleanup import cleanup

from general.models import AuthorCreatedAt
from .services import success_created_collect_email, success_created_payment_email


class Event(models.Model):
    title = models.CharField('Событие', max_length=256, unique=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = "События"

    def __str__(self):
        return self.title


class Payment(AuthorCreatedAt):
    amount = models.DecimalField('Сумма доната', max_digits=9, decimal_places=2)
    message = models.TextField('Сообщение', blank=True, null=True)
    collect = models.ForeignKey('Collect', on_delete=models.PROTECT, verbose_name='Платежи')

    class Meta:
        default_related_name = 'payments'
        verbose_name = 'Донат'
        verbose_name_plural = "Донаты"


@cleanup.select
class Collect(AuthorCreatedAt):
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    image = models.ImageField('Картинка', upload_to='img/%Y')
    required_amount = models.DecimalField('Необходимая сумма', max_digits=15, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, verbose_name='Событие')
    finished_at = models.DateTimeField('Конец сбора')

    class Meta:
        default_related_name = 'collects'
        verbose_name = 'Сбор'
        verbose_name_plural = 'Сборы'

    def __str__(self):
        return self.title


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
