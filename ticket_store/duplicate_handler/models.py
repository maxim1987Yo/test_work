from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class DuplicateHandlerStatus(models.IntegerChoices):
    CREATED = 1, 'Создан'
    SUCCESS = 2, 'Закончен успешно'
    FAILED = 3, 'Закончен с ошибкой'


class DuplicateHandler(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name='таблица',
    )
    original_object_id = models.PositiveIntegerField(verbose_name='оригинал')
    original = GenericForeignKey('content_type', 'original_object_id')
    replacement_object_id = models.PositiveIntegerField(verbose_name='замена')
    replacement = GenericForeignKey('content_type', 'replacement_object_id')
    status = models.IntegerField(
        verbose_name='статус обработки',
        choices=DuplicateHandlerStatus.choices,
        default=DuplicateHandlerStatus.CREATED,
    )
    result = models.TextField(
        verbose_name='результат',
        null=True,
        blank=True,
    )
    errors = models.TextField(
        verbose_name='ошибки',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'обработка дубля'
        verbose_name_plural = 'обработки дублей'

    def __str__(self):
        return f'{self.content_type}'