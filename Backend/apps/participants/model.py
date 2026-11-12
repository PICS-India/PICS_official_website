
from django.db import models

class Participant(models.Model):

    YEAR_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
        ('Other', 'Other'),
    ]

    full_name = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    college = models.CharField(max_length=200)

    department = models.CharField(max_length=100)

    academic_year = models.CharField(
        max_length=20,
        choices=YEAR_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'participants'
        ordering = ['full_name']