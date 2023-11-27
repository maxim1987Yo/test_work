from django.db import models


class Route(models.Model):
    """Маршрут между двумя остановками"""
    company = models.ForeignKey(
        'core.Company',
        verbose_name='Компания',
        on_delete=models.CASCADE,
    )
    start_stop = models.ForeignKey(
        'core.Stop',
        related_name='start_stop',
        verbose_name='Начальная остановка',
        on_delete=models.CASCADE,
    )
    end_stop = models.ForeignKey(
        'core.Stop',
        related_name='end_stop',
        verbose_name='Конечная остановка',
        on_delete=models.CASCADE,
    )
    duration = models.DurationField(verbose_name='Продолжительность поездки')

    class Meta:
        verbose_name = 'Маршрут между двумя остановками'
        verbose_name_plural = 'Маршруты между двумя остановками'

    def __str__(self):
        return f'Маршрут между двумя остановками {self.pk}'
