from django.test import TestCase

from .participant_models import Participant


class ParticipantModelTests(TestCase):

    def setUp(self):
        self.participant = Participant.objects.create(
            full_name="Vedant Narkhede",
            email="vedant@example.com",
            phone="9876543210",
            college_name="DY Patil International University",
            department="Computer Science",
            academic_year="second",
            city="Pune",
            state="Maharashtra",
        )

    def test_participant_creation(self):
        self.assertEqual(
            self.participant.full_name,
            "Vedant Narkhede"
        )

    def test_participant_email(self):
        self.assertEqual(
            self.participant.email,
            "vedant@example.com"
        )

    def test_participant_default_verification(self):
        self.assertFalse(self.participant.is_verified)

    def test_participant_database_table(self):
        self.assertEqual(
            self.participant._meta.db_table,
            "pics_participants"
        )

    def test_participant_string_representation(self):
        self.assertEqual(
            str(self.participant),
            "Vedant Narkhede (vedant@example.com)"
        )
# This is Temp, after i will integrrate thiis database