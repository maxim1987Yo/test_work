from django.db import models


class Schedule(models.Model):
    """Расписание автобусов"""
    company = models.ForeignKey(
        'core.Company',
        verbose_name='компания',
        on_delete=models.CASCADE,
    )
    bus = models.ForeignKey(
        'core.Bus',
        verbose_name='автобус',
        on_delete=models.CASCADE,
    )
    route = models.ForeignKey(
        'core.Route',
        verbose_name='маршрут',
        on_delete=models.CASCADE,
    )
    departure_time = models.DateTimeField(verbose_name='Время отправления')
    arrival_time = models.DateTimeField(verbose_name='Время прибытия')
    price = models.DecimalField(
        verbose_name='Цена билета',
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'Расписание автобусов'
        verbose_name_plural = 'Расписания автобусов'
