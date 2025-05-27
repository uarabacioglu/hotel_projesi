from django.db import models


class Pool(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="indoor, outdoor, children etc.",
    )
    image = models.ImageField(
        width_field="700",
        height_field="500",
        upload_to="pools",
    )
    opening_time = models.CharField(
        max_length=5,
        help_text="09:00",
    )
    closing_time = models.CharField(
        max_length=5,
        help_text="19:00",
    )

    class Meta:
        db_table = "pools"
        verbose_name = "Pool"
        verbose_name_plural = "Pools"

    def __str__(self):
        return str(self.title)
