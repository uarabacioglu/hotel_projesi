import uuid
from django.db import models

from hotels.models.room_periods import PeriodPricing


class BlockDates(models.Model):
    period_pricing = models.ForeignKey(
        to=PeriodPricing, on_delete=models.CASCADE, related_name="period_blokdates"
    )
    blocked_date = models.DateField(
        auto_now=False,
        blank=False,
        null=False,
    )

    class Meta:
        db_table = "blocked_dates"
        verbose_name = "Blocked Date"
        verbose_name_plural = "Blocked Dates"

    def __str__(self):
        return f"{self.period_pricing.title} - {self.blocked_date}"
