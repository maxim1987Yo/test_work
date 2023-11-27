from django.db import models


class Company(models.Model):
    """Информация о транспортной компании"""
    name = models.CharField(verbose_name='название', max_length=100)
    address = models.CharField(verbose_name='адрес', max_length=255)
    phone = models.CharField(verbose_name='контактный телефон', max_length=20)
    email = models.EmailField(verbose_name='электронная почта')

    class Meta:
        verbose_name = 'транспортная компания'
        verbose_name_plural = 'транспортные компании'

    def __str__(self):
        return f'транспортная компания {self.pk}'
