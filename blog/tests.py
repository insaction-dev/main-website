from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Category, Article

# Create your tests here.


class ProfileTest(TestCase):
    def setUp(self):
        user_john = User.objects.create_user(
            'johndoe', 'john@gmail.com', None, first_name="John", last_name="Doe")
        user_solar = User.objects.create_user(
            'solarliner', 'solarliner@gmail.com', None, first_name="Nathan", last_name="Graule")
        self.john = Profile.profiles.create(user=user_john, campus='blois')
        self.solar = Profile.profiles.create(user=user_solar, campus='bourges')

    def test_full_name(self):
        """Profile has a `full_name` property that returns the full name."""
        self.assertEqual(self.john.full_name, "John Doe")
        self.assertEqual(self.solar.full_name, "Nathan Graule")

    def test_short_full_name(self):
        """Profile has a `short_full_name` property that returns the first letter of the first name, and the complete last name."""
        self.assertEqual(self.john.full_name_short, "J. Doe")
        self.assertEqual(self.solar.full_name_short, "N. Graule")

    def test_str(self):
        """Profile, when cast to string, should be the full name of the underlying `User`."""
        self.assertEqual(str(self.john), "J. Doe")
        self.assertEqual(str(self.solar), "N. Graule")


class CategoryTest(TestCase):
    def setUp(self):
        self.cat_short = Category.categories.create(name='Short blog name', description='Short name category')
        long_title = 'a' * 55
        self.cat_long = Category.categories.create(name=long_title, description='Long name category')
    
    def test_slugify(self):
        """Categories should have correctly formed slugs"""
        self.assertEqual(self.cat_short.slug, 'short-blog-name')
        regex = r'[@:%._\+~#=]+'
        self.assertNotRegex(self.cat_short.slug, regex)
        self.assertNotRegex(self.cat_long.slug, regex)
    
    def test_slugs_max_length(self):
        """Categories should have slugs with length less than 50 characters"""
        self.assertLessEqual(len(str(self.cat_short.slug)), 50)
        self.assertLessEqual(len(str(self.cat_long.slug)), 50)

    def test_slugs_truncate(self):
        """Long category names should have slugs truncated"""
        self.assertFalse(str(self.cat_long.slug).endswith('a' * 8))
        self.assertTrue(str(self.cat_short.slug).endswith('-name'))
