from django.db import models
from django_cleanup import cleanup

from general.models import AuthorCreatedAt


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

    def __str__(self):
        return f'{self.collect} - {self.amount}'


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


