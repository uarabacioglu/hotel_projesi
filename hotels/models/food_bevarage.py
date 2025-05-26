from django.db import models


class FoodBevarage(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="lobby bar, italyan restoran, ana rest.",
    )
    is_free = models.BooleanField(
        default=True,
        help_text="ücretliyse false yap!",
    )
    image = models.ImageField(
        width_field="700",
        height_field="500",
        upload_to="foodbevarages",
    )

    class Meta:
        db_table = "food_bevarage"
        verbose_name = "Food & Bevarage"
        verbose_name_plural = "Food & Bevarages"

    def __str__(self):
        return str(self.title)
