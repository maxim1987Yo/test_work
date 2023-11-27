from django.db import models


class RouteStop(models.Model):
    """Промежуточные остановки на маршруте"""
    route = models.ForeignKey(
        'core.Route',
        verbose_name='Маршрут',
        on_delete=models.CASCADE,
    )
    stop = models.ForeignKey(
        'core.Stop',
        verbose_name='Остановка',
        on_delete=models.CASCADE,
    )
    index = models.IntegerField(verbose_name='Порядковый номер остановки на маршруте')
    distance = models.DecimalField(
        verbose_name='Километраж от начальной точки',
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'Промежуточная остановка на маршруте'
        verbose_name_plural = 'Промежуточные остановки на маршруте'

    def __str__(self):
        return f'Промежуточная остановка на маршруте {self.pk}'
