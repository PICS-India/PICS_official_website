from django.db import transaction

from .payment_models import Payment


@transaction.atomic
def mark_payment_success(payment_id, transaction_id, provider=""):

    payment = Payment.objects.select_for_update().get(
        id=payment_id
    )

    if payment.payment_status != "pending":
        raise ValueError("Only pending payments can be updated.")

    payment.payment_status = "success"
    payment.transaction_id = transaction_id
    payment.provider = provider

    payment.save(
        update_fields=[
            "payment_status",
            "transaction_id",
            "provider",
            "updated_at"
        ]
    )

    return payment


@transaction.atomic
def mark_payment_failed(payment_id):

    payment = Payment.objects.select_for_update().get(
        id=payment_id
    )

    if payment.payment_status != "pending":
        raise ValueError("Only pending payments can be updated.")

    payment.payment_status = "failed"

    payment.save(
        update_fields=[
            "payment_status",
            "updated_at"
        ]
    )

    return payment