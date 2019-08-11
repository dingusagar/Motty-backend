import factory

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username{0}'.format(n))
    first_name = factory.Sequence(lambda n: 'firstname{0}'.format(n))
    last_name = factory.Sequence(lambda n: 'lastname{0}'.format(n))
    email = factory.Sequence(lambda n: 'xyz{0}@company{0}.com'.format(n))




