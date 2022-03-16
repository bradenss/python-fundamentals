# 11-1
# 1
import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        anchorage_alaska = city_country('anchorage', 'alaska')
        self.assertEqual(anchorage_alaska, 'Anchorage, Alaska')


unittest.main()

# 11-2
# 2


import unittest

from city_functions import city_country1


class CitiesTestCase1(unittest.TestCase):

    def test_city_country(self):
        anchorage_alaska = city_country1('anchorage', 'alaska', 500000)
        self.assertEqual(anchorage_alaska, 'Anchorage, Alaska')

    def test_city_country_population(self):
        anchorage_alaska = city_country1('anchorage', 'alaska', population=500000)
        self.assertEqual(anchorage_alaska, 'Anchorage, Alaska - population 500000')


unittest.main()

# 11-3
# 3

import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.jane = Employee('jane', 'doe', 50000)

    def test_give_default_raise(self):
        self.jane.give_raise()
        self.assertEqual(self.jane.salary, 55000)

    def test_give_custom_raise(self):
        self.jane.give_raise(2500)
        self.assertEqual(self.jane.salary, 55000)


unittest.main()
