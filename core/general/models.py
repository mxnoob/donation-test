from django.conf import settings
from django.db import models


class AuthorCreatedAt(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        abstract = True
