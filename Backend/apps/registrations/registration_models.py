from django.db import models


class Registration(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    PAYMENT_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
        ("not_required", "Not Required"),
    ]

    participant = models.ForeignKey(
        "pics_participants.Participant",
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    event = models.ForeignKey(
        "pics_events.Event",
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="pending"
    )

    amount_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.participant.full_name} - {self.event.title}"

    class Meta:
        db_table = "pics_registrations"
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["participant", "event"],
                name="unique_participant_event_registration"
            )
        ]