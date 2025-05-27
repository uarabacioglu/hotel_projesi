import uuid
from django.db import models
from hotels.models.room_base import Room


class PeriodPricing(models.Model):
    CURRENCY_LIST = (
        ("EUR", "EUR"),
        ("GBP", "GBP"),
        ("USD", "USD"),
    )

    period_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    room = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
        related_name="room_periods",
    )

    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="sea view",
    )

    description = models.TextField(
        max_length=2000,
        help_text="sea view with twin beds",
    )

    start_date = models.DateField(
        auto_now=False,
    )

    end_date = models.DateField(
        auto_now=False,
    )

    currency = models.CharField(
        choices=CURRENCY_LIST,
        default="EUR",
    )

    pp_net_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=False,
        null=False,
        default=0.0,
        help_text="per person gecelik net fiyat",
    )

    pp_retail_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=False,
        null=False,
        default=0.0,
        help_text="per person gecelik satış fiyatı",
    )

    discount_rate = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="indirim oranı tüm katılımcıların toplam rezervasyon tutarında yüzdelik olarak düşülücek.",
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "periods"
        verbose_name = "Period Pricing"
        verbose_name_plural = "PeriodS PricingS"

    def __str__(self):
        return f"{self.room.title} - {self.start_date} - {self.end_date}"
