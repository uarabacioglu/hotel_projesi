from django.db import models


class Beach(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="private, sand, stone..",
    )
    distance_hotel = models.CharField(
        max_length=256,
        help_text="250 mt to hotel",
    )
    image = models.ImageField(
        upload_to="beach_images",
        blank=False,
        null=False,
    )
    date_added = models.DateField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "beach"
        verbose_name = "Beach"
        verbose_name_plural = "Beach"

    def __str__(self):
        return f"{self.title}"
