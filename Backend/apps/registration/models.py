
from django.db import models

class Registration(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    participant = models.ForeignKey(
        'participants.Participant',
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    registration_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.participant.full_name} - {self.event.title}"

    class Meta:
        db_table = 'registrations'
        ordering = ['-registration_date']

        # One participant can register only once for an event
        constraints = [
            models.UniqueConstraint(
                fields=['participant', 'event'],
                name='unique_participant_event'
            )
        ]