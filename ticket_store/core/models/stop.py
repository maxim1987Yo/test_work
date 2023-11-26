from django.db import models


class Stop(models.Model):
    """Информация об остановке"""
    name = models.CharField(verbose_name='название', max_length=100)
    location = models.CharField(verbose_name='местоположение', max_length=255)

    class Meta:
        verbose_name = 'остановка'
        verbose_name_plural = 'остановки'
