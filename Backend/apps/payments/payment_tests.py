from django.test import TestCase

from apps.events.event_models import Event
from apps.participants.participant_models import Participant
from apps.registrations.registration_models import Registration

from .payment_models import Payment


class PaymentTests(TestCase):

    def setUp(self):

        self.participant = Participant.objects.create(
            full_name="Test User",
            email="payment@example.com",
            phone="9876543210"
        )

        self.event = Event.objects.create(
            title="Test Event",
            description="Payment testing event",
            venue="Pune",
            start_date="2027-01-10",
            end_date="2027-01-11",
            registration_start="2026-12-01",
            registration_end="2027-01-05"
        )

        self.registration = Registration.objects.create(
            participant=self.participant,
            event=self.event
        )

        self.payment = Payment.objects.create(
            registration=self.registration,
            amount=500,
            payment_method="upi"
        )

    def test_payment_creation(self):

        self.assertEqual(
            self.payment.amount,
            500
        )

    def test_payment_default_status(self):

        self.assertEqual(
            self.payment.payment_status,
            "pending"
        )