from django.db import models
from django.db.models import CheckConstraint, Q


class Bus(models.Model):
    """Информация об автобусе, принадлежащем компании"""
    company = models.ForeignKey(
        'core.Company',
        verbose_name='транспортная компания',
        on_delete=models.CASCADE,
    )
    number = models.CharField(verbose_name='номер', max_length=50)
    model = models.CharField(verbose_name='модель', max_length=100)
    capacity = models.IntegerField(verbose_name='вместимость')

    class Meta:
        verbose_name = 'автобус'
        verbose_name_plural = 'автобусы'
        constraints = [
            CheckConstraint(
                check=Q(capacity__gt=0),
                name='bus_capacity_more_zero',
                violation_error_message='Вместимость автобуса не может быть меньше 1',
            ),
        ]

    def __str__(self):
        return f'автобус {self.pk}'
