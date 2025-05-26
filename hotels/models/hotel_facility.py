from django.db import models


class GeneralFacility(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="pool, spa, gym",
    )
    is_free = models.BooleanField(
        default=True,
        help_text="ücretliyse false yap!",
    )
    image = models.ImageField(
        upload_to="general_facility",
    )

    class Meta:
        db_table = "general_facility"
        verbose_name = "General Facility"
        verbose_name_plural = "General Facilities"

    def __str__(self):
        return str(self.title)
