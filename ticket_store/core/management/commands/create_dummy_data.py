from django.core.management.base import BaseCommand
import factory.fuzzy

from core.services.factory import StopFactory, CompanyFactory, BusFactory, RouteFactory, RouteStopFactory, \
    ScheduleFactory, UserFactory, TicketFactory


class Command(BaseCommand):
    help = 'Наполняет таблицы сгенерированными данными'

    def handle(self, *args, **options):
        stop = StopFactory.create_batch(1000)
        company = CompanyFactory.create_batch(1000)
        bus = BusFactory.create_batch(3000, company=factory.fuzzy.FuzzyChoice(company))
        route = RouteFactory.create_batch(
            5000,
            company=factory.fuzzy.FuzzyChoice(company),
            start_stop=factory.fuzzy.FuzzyChoice(stop),
            end_stop=factory.fuzzy.FuzzyChoice(stop),
        )
        RouteStopFactory.create_batch(
            3000,
            route=factory.fuzzy.FuzzyChoice(route),
            stop=factory.fuzzy.FuzzyChoice(stop),
        )
        schedule = ScheduleFactory.create_batch(
            3000,
            company=factory.fuzzy.FuzzyChoice(company),
            bus=factory.fuzzy.FuzzyChoice(bus),
            route=factory.fuzzy.FuzzyChoice(route),
        )
        user = UserFactory.create_batch(1000)
        TicketFactory.create_batch(
            3000,
            company=factory.fuzzy.FuzzyChoice(company),
            user=factory.fuzzy.FuzzyChoice(user),
            schedule=factory.fuzzy.FuzzyChoice(schedule),
        )
