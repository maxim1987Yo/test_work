import factory
import factory.fuzzy
from django.contrib.auth import get_user_model

from core.models import Company, Bus, Stop, Schedule, RouteStop, Route
from core.models.ticket import TicketStatus, Ticket


class BusFactory(factory.django.DjangoModelFactory):
    company = None
    number = factory.Faker('company')
    model = factory.Faker('company')
    capacity = 30

    class Meta:
        model = Bus


class StopFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('company')
    location = factory.Faker('address')

    class Meta:
        model = Stop


class CompanyFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('company')
    address = factory.Faker('address')
    phone = factory.Faker('phone_number', locale='ru')
    email = factory.Faker('email')

    class Meta:
        model = Company


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('email')
    email = factory.Faker('email')

    class Meta:
        model = get_user_model()
        django_get_or_create = ('username',)


class TicketFactory(factory.django.DjangoModelFactory):
    company = None
    user = None
    schedule = None
    seat_number = factory.fuzzy.FuzzyInteger(45)
    status = factory.fuzzy.FuzzyChoice(choices=[i[0] for i in TicketStatus.choices])
    purchase_time = factory.Faker('date_time')

    class Meta:
        model = Ticket


class ScheduleFactory(factory.django.DjangoModelFactory):
    company = None
    bus = None
    route = None
    departure_time = factory.Faker('date_time')
    arrival_time = factory.Faker('date_time')
    price = factory.fuzzy.FuzzyInteger(456)

    class Meta:
        model = Schedule


class RouteStopFactory(factory.django.DjangoModelFactory):
    route = None
    stop = None
    index = factory.fuzzy.FuzzyInteger(45)
    distance = factory.fuzzy.FuzzyInteger(456)

    class Meta:
        model = RouteStop


class RouteFactory(factory.django.DjangoModelFactory):
    company = None
    start_stop = None
    end_stop = None
    duration = '3 hours'

    class Meta:
        model = Route


