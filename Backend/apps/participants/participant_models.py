from django.db import models


class Participant(models.Model):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
        ("prefer_not_to_say", "Prefer not to say"),
    ]

    YEAR_CHOICES = [
        ("first", "First Year"),
        ("second", "Second Year"),
        ("third", "Third Year"),
        ("fourth", "Fourth Year"),
        ("other", "Other"),
    ]

    full_name = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    gender = models.CharField(
        max_length=25,
        choices=GENDER_CHOICES,
        blank=True
    )

    college_name = models.CharField(max_length=200)

    department = models.CharField(max_length=100)

    academic_year = models.CharField(
        max_length=20,
        choices=YEAR_CHOICES,
        default="other"
    )

    city = models.CharField(max_length=100, blank=True)

    state = models.CharField(max_length=100, blank=True)

    profile_image = models.ImageField(
        upload_to="participants/profiles/",
        blank=True,
        null=True
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    class Meta:
        db_table = "pics_participants"
        ordering = ["-created_at"]
        verbose_name = "Participant"
        verbose_name_plural = "Participants"
