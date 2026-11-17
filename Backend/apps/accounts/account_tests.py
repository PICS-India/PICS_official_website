from django.test import TestCase
from django.contrib.auth.models import User

from .account_models import AccountProfile


class AccountTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="TestPassword123!"
        )

        self.profile = AccountProfile.objects.create(
            user=self.user,
            phone="9876543210"
        )

    def test_account_creation(self):

        self.assertEqual(
            self.profile.user.username,
            "testuser"
        )

    def test_account_email(self):

        self.assertEqual(
            self.user.email,
            "test@example.com"
        )

    def test_account_profile(self):

        self.assertEqual(
            self.profile.phone,
            "9876543210"
        )