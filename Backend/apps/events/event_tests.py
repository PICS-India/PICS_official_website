from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from .event_models import Event


class EventModelTests(TestCase):

    def setUp(self):
        start = timezone.now() + timedelta(days=10)

        self.event = Event.objects.create(
            title="PICS Technical Fest",
            description="Annual technical event.",
            category="Technical",
            venue="DYPIU Akurdi",
            mode="offline",
            start_date=start,
            end_date=start + timedelta(hours=5),
            capacity=100,
            registration_fee=0,
        )

    def test_event_creation(self):
        self.assertEqual(
            self.event.title,
            "PICS Technical Fest"
        )

    def test_event_slug_creation(self):
        self.assertTrue(self.event.slug)

    def test_event_database_table(self):
        self.assertEqual(
            self.event._meta.db_table,
            "pics_events"
        )

    def test_event_status_default(self):
        self.assertEqual(
            self.event.status,
            "upcoming"
        )
