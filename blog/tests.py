import random
import os
import pathlib


from django.test import TestCase
import faker
# Create your tests here.

# a = os.path.join('a', 'b', 'c')
# b = pathlib.Path('a').joinpath('b', 'c').rea
# print(a)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    # django.setup()
    # from django.utils import timezone
    # fake = faker.Faker()
    # print(timezone.get_current_timezone())
    #
    # created_time = fake.date_time_between(start_date='-1y', end_date="now",
    #                                       tzinfo=timezone.get_current_timezone())
    # print(created_time)
    for i in range(5):
        print(random.randrange(3,15))
        print(random.randint(1, 5))