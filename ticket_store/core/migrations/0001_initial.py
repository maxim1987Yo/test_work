# Generated by Django 4.2.7 on 2023-11-26 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=50, verbose_name="номер")),
                ("model", models.CharField(max_length=100, verbose_name="модель")),
                ("capacity", models.IntegerField(verbose_name="вместимость")),
            ],
            options={"verbose_name": "автобус", "verbose_name_plural": "автобусы",},
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="название")),
                ("address", models.CharField(max_length=255, verbose_name="адрес")),
                (
                    "phone",
                    models.CharField(max_length=20, verbose_name="контактный телефон"),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="электронная почта"),
                ),
            ],
            options={
                "verbose_name": "транспортная компания",
                "verbose_name_plural": "транспортные компании",
            },
        ),
        migrations.CreateModel(
            name="Route",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "duration",
                    models.DurationField(verbose_name="Продолжительность поездки"),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.company",
                        verbose_name="Компания",
                    ),
                ),
            ],
            options={
                "verbose_name": "Маршрут между двумя остановками",
                "verbose_name_plural": "Маршруты между двумя остановками",
            },
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "departure_time",
                    models.DateTimeField(verbose_name="Время отправления"),
                ),
                ("arrival_time", models.DateTimeField(verbose_name="Время прибытия")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена билета"
                    ),
                ),
                (
                    "bus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.bus",
                        verbose_name="автобус",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.company",
                        verbose_name="компания",
                    ),
                ),
                (
                    "route",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.route",
                        verbose_name="маршрут",
                    ),
                ),
            ],
            options={
                "verbose_name": "Расписание автобусов",
                "verbose_name_plural": "Расписания автобусов",
            },
        ),
        migrations.CreateModel(
            name="Stop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="название")),
                (
                    "location",
                    models.CharField(max_length=255, verbose_name="местоположение"),
                ),
            ],
            options={"verbose_name": "остановка", "verbose_name_plural": "остановки",},
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seat_number", models.IntegerField(verbose_name="номер места")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("booked", "забронирован"),
                            ("purchased", "куплен"),
                            ("cancelled", "отменен"),
                        ],
                        max_length=50,
                        verbose_name="",
                    ),
                ),
                (
                    "purchase_time",
                    models.DateTimeField(verbose_name="Время покупки билета"),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.company",
                        verbose_name="кампания",
                    ),
                ),
                (
                    "schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.schedule",
                        verbose_name="расписание",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пассажир",
                    ),
                ),
            ],
            options={"verbose_name": "Информация о билете на автобус",},
        ),
        migrations.CreateModel(
            name="RouteStop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "index",
                    models.IntegerField(
                        verbose_name="Порядковый номер остановки на маршруте"
                    ),
                ),
                (
                    "distance",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Километраж от начальной точки",
                    ),
                ),
                (
                    "route",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.route",
                        verbose_name="Маршрут",
                    ),
                ),
                (
                    "stop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.stop",
                        verbose_name="Остановка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Промежуточная остановка на маршруте",
                "verbose_name_plural": "Промежуточные остановки на маршруте",
            },
        ),
        migrations.AddField(
            model_name="route",
            name="end_stop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="end_stop",
                to="core.stop",
                verbose_name="Конечная остановка",
            ),
        ),
        migrations.AddField(
            model_name="route",
            name="start_stop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="start_stop",
                to="core.stop",
                verbose_name="Начальная остановка",
            ),
        ),
        migrations.AddField(
            model_name="bus",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.company",
                verbose_name="транспортная компания",
            ),
        ),
        migrations.AddConstraint(
            model_name="bus",
            constraint=models.CheckConstraint(
                check=models.Q(("capacity__gt", 0)),
                name="bus_capacity_more_zero",
                violation_error_message="Вместимость автобуса не может быть меньше 1",
            ),
        ),
    ]