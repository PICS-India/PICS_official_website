from django.db import models
from django.utils.text import slugify


class Event(models.Model):

    STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    MODE_CHOICES = [
        ("online", "Online"),
        ("offline", "Offline"),
        ("hybrid", "Hybrid"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    description = models.TextField()
    category = models.CharField(max_length=100)

    venue = models.CharField(max_length=255, blank=True)
    mode = models.CharField(
        max_length=20,
        choices=MODE_CHOICES,
        default="offline"
    )

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    registration_start = models.DateTimeField(null=True, blank=True)
    registration_end = models.DateTimeField(null=True, blank=True)

    capacity = models.PositiveIntegerField(default=100)
    registration_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="upcoming"
    )

    banner = models.ImageField(
        upload_to="events/banners/",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            counter = 1

            while Event.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "pics_events"
        ordering = ["-start_date"]
