from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="adults only, familiy friendly",
    )
    description = models.TextField(
        max_length=2000,
    )
    image = models.ImageField(
        upload_to="cat_images",
        blank=False,
        null=False,
    )
    date_added = models.DateField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.title}"
