
from django.test import TestCase
from models import Participant

class ParticipantModelTest(TestCase):

    def setUp(self):

        self.participant = Participant.objects.create(
            full_name='Vedant Narkhede',
            email='vedant@example.com',
            phone='9876543210',
            college='DYPIU Akurdi',
            department='Computer Science',
            academic_year='2nd Year'
        )

    def test_participant_creation(self):

        self.assertEqual(
            self.participant.full_name,
            'Vedant Narkhede'
        )

    def test_participant_email(self):

        self.assertEqual(
            self.participant.email,
            'vedant@example.com'
        )

    def test_participant_string(self):

        self.assertEqual(
            str(self.participant),
            'Vedant Narkhede'
        )