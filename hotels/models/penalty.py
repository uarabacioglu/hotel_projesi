from django.db import models


class Penalty(models.Model):
    title = models.CharField(
    max_length=256,
    help_text="full, partial refund",
    )
    description = models.TextField(
        max_length=2000,
    )
    before_check_in = models.PositiveIntegerField(
        default=0,
        help_text="girişten kaç gün öncesine kadar?",
    )
    cancellation_fee = models.PositiveIntegerField(
        default = 0,
        max_length=100,
    )

    class Meta:
        db_table="penalty"
        verbose_name="Penalty"
        verbose_name_plural="Penalties"
