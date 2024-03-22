from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Event(models.Model):
    title = models.CharField('Событие', max_length=256, unique=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = "События"

    def __str__(self):
        return self.title


class Payment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='payments', verbose_name='Донатер')
    amount = models.DecimalField('Сумма доната', max_digits=9, decimal_places=2)
    message = models.TextField('Сообщение', blank=True, null=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    collect = models.ForeignKey('Collect', on_delete=models.PROTECT, related_name='payments', verbose_name='Платежи')

    class Meta:
        verbose_name = 'Донат'
        verbose_name_plural = "Донаты"


class Collect(models.Model):
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    image = models.ImageField('Картинка', upload_to='img/%Y')
    required_amount = models.DecimalField('Необходимая сумма', max_digits=15, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='collects', verbose_name='Автор сбора')
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='collects', verbose_name='Событие')
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    finished_at = models.DateTimeField('Конец сбора')

    class Meta:
        verbose_name = 'Сбор'
        verbose_name_plural = 'Сборы'

    def __str__(self):
        return self.title


class CollectPayment(models.Model):
    collect = models.ForeignKey(Collect, on_delete=models.PROTECT)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)
