from django.contrib.auth import get_user_model
from django.db import models


class TicketStatus(models.TextChoices):
    BOOKED = 'booked', 'забронирован',
    PURCHASED = 'purchased', 'куплен',
    CANCELLED = 'cancelled', 'отменен',


class Ticket(models.Model):
    """Информация о билете на автобус"""
    company = models.ForeignKey(
        'core.Company',
        verbose_name='кампания',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='пассажир',
        on_delete=models.CASCADE,
    )
    schedule = models.ForeignKey(
        'core.Schedule',
        verbose_name='расписание',
        on_delete=models.CASCADE,
    )
    seat_number = models.IntegerField(verbose_name='номер места')
    status = models.CharField(
        verbose_name='',
        choices=TicketStatus.choices,
        max_length=50,
    )
    purchase_time = models.DateTimeField(verbose_name='Время покупки билета')

    class Meta:
        verbose_name = 'Информация о билете на автобус'
