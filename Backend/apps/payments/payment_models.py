from django.db import models

from apps.registrations.registration_models import Registration


class Payment(models.Model):

    PAYMENT_STATUS = [
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]

    PAYMENT_METHOD = [
        ("online", "Online"),
        ("upi", "UPI"),
        ("card", "Card"),
        ("netbanking", "Net Banking"),
        ("other", "Other"),
    ]

    registration = models.ForeignKey(
        Registration,
        on_delete=models.PROTECT,
        related_name="payments"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD,
        default="online"
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="pending"
    )

    transaction_id = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True
    )

    provider = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"Payment {self.id} - {self.payment_status}"

    class Meta:

        db_table = "pics_payments"

        ordering = ["-created_at"]