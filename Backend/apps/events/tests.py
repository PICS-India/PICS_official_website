
from django.test import TestCase
from .models import Event
from datetime import date, time

class EventModelTest(TestCase):

    def setUp(self):

        self.event = Event.objects.create(
            title='PICS Technical Event',
            description='A technical event',
            event_date=date(2026, 12, 15),
            start_time=time(10, 0),
            end_time=time(17, 0),
            venue='Pune',
            status='upcoming'
        )

    def test_event_creation(self):

        self.assertEqual(
            self.event.title,
            'PICS Technical Event'
        )

    def test_event_string(self):

        self.assertEqual(
            str(self.event),
            'PICS Technical Event'
        )