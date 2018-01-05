from django.test import TestCase
from .models import UserProxy

# Create your tests here.


class UserProxyTest(TestCase):
    def setUp(self):
        self.john = UserProxy.objects.create_user(
            'johndoe', 'john@gmail.com', None, first_name="John", last_name="Doe")
        self.solar = UserProxy.objects.create_user(
            'solarliner', 'solarliner@gmail.com', None, first_name="Nathan", last_name="Graule")

    def test_full_name(self):
        """UserProxy has a `full_name` property that returns the full name."""
        # john = UserProxy.objects.get_by_natural_key('johndoe')
        # solar = UserProxy.objects.get_by_natural_key('solarliner')
        self.assertEqual(self.john.full_name, "John Doe")
        self.assertEqual(self.solar.full_name, "Nathan Graule")

    def test_short_full_name(self):
        """UserProxy has a `short_full_name` property that returns the first letter of the first name, and the complete last name."""
        self.assertEqual(self.john.full_name_short, "J. Doe")
        self.assertEqual(self.solar.full_name_short, "N. Graule")

    def test_str(self):
        """UserProxy, when cast to string, should be the full name of the underlying `User`."""
        self.assertEqual(str(self.john), "J. Doe")
        self.assertEqual(str(self.solar), "N. Graule")
