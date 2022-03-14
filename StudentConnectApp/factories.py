import factory
from factory.django import DjangoModelFactory
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from StudentConnectApp.models import Student, Answer

@factory.django.mute_signals(post_save)
class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student
    
    user = factory.SubFactory('StudentConnectApp.factories.UserFactory', profile=None)
    forename = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    date_of_birth = factory.Faker("date_of_birth")

@factory.django.mute_signals(post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_%d" % n)

    profile = factory.RelatedFactory(StudentFactory, factory_related_name='user')

class AnswerFactory(DjangoModelFactory):
    class Meta:
        model = Answer

    