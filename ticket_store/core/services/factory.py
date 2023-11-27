import factory


from core.models import Company, Bus


class BusFactory(factory.django.DjangoModelFactory):
    company = None
    number = factory.Faker('company')
    model = factory.Faker('company')
    capacity = 30

    class Meta:
        model = Bus


class CompanyFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('company')
    address = factory.Faker('address')
    phone = factory.Faker('phone_number', locale='ru')
    email = factory.Faker('email')

    class Meta:
        model = Company

    @factory.post_generation
    def post_related_models(obj, create, extracted, **kwargs):
        if not create:
            return
        BusFactory.create(
            company=obj
        )

# from core.services.factory import *
# CompanyFactory.create_batch(500)
