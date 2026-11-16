from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from apps.participants.participant_models import Participant
from apps.events.event_models import Event
from .registration_models import Registration


class RegistrationTests(TestCase):

    def setUp(self):

        self.participant = Participant.objects.create(
            full_name="Test User",
            email="test@example.com",
            phone="9876543210"
        )

        now = timezone.now()

        self.event = Event.objects.create(
            title="Python Workshop",
            category="Workshop",
            venue="Pune",
            mode="offline",
            start_date=now + timedelta(days=10),
            end_date=now + timedelta(days=11),
            registration_start=now,
            registration_end=now + timedelta(days=5),
            capacity=100,
            registration_fee=0
        )

    def test_registration_creation(self):

        registration = Registration.objects.create(
            participant=self.participant,
            event=self.event
        )

        self.assertEqual(
            registration.status,
            "pending"
        )

        self.assertEqual(
            registration.payment_status,
            "pending"
        )

    def test_registration_relation(self):

        registration = Registration.objects.create(
            participant=self.participant,
            event=self.event
        )

        self.assertEqual(
            registration.participant,
            self.participant
        )

        self.assertEqual(
            registration.event,
            self.event
        )