
from django.test import TestCase
from datetime import date, time

from apps.events.models import Event
from apps.participants.models import Participant
from .models import Registration

class RegistrationModelTest(TestCase):

    def setUp(self):

        self.participant = Participant.objects.create(
            full_name='Vedant Narkhede',
            email='vedant@example.com',
            phone='9876543210',
            college='DYPIU Akurdi',
            department='Computer Science',
            academic_year='2nd Year'
        )

        self.event = Event.objects.create(
            title='PICS Technical Event',
            description='Technical event',
            event_date=date(2026, 12, 15),
            start_time=time(10, 0),
            end_time=time(17, 0),
            venue='Pune',
            status='upcoming',
            is_registration_open=True
        )

    def test_registration_creation(self):

        registration = Registration.objects.create(
            participant=self.participant,
            event=self.event
        )

        self.assertEqual(
            registration.status,
            'pending'
        )

    def test_registration_string(self):

        registration = Registration.objects.create(
            participant=self.participant,
            event=self.event
        )

        self.assertEqual(
            str(registration),
            'Vedant Narkhede - PICS Technical Event'
        )