import factory
from users.factories import UserFactory

from .models import Collect, Event, Payment


class EventFactory(factory.django.DjangoModelFactory):
    title = factory.Faker(
        'random_element',
        elements=['weeding', 'birthday', 'science', 'baby', 'education'],
    )

    class Meta:
        model = Event


class CollectFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    event = factory.SubFactory(EventFactory)
    title = factory.Faker('sentence')
    description = factory.Faker('paragraph')
    image = factory.Faker('image_url')
    required_amount = factory.Faker('random_number', digits=5)

    class Meta:
        model = Collect


class PaymentFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    collect = factory.SubFactory(CollectFactory)
    amount = factory.Faker('random_number', digits=3)
    message = factory.Faker('words')

    class Meta:
        model = Payment
