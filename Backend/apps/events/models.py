
from django.db import models


class Event(models.Model):

    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.URLField(blank=True, null=True)

    event_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    venue = models.CharField(max_length=255)

    registration_deadline = models.DateTimeField(
        blank=True,
        null=True
    )

    max_participants = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='upcoming'
    )

    is_registration_open = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-event_date']
        db_table = 'events'
