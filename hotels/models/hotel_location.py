from django.db import models


class LocationDetails(models.Model):
    google_map_url = models.URLField(
        max_length=1000,
        blank=False,
        null=False,
        help_text="http://map.google.com/en-boy",
    )
    zip_code = models.CharField(
        max_length=7,
        blank=False,
        null=False,
        help_text="07330",
    )
    to_airport = models.CharField(
        max_length=64,
        help_text="70 km",
    )
    to_beach = models.CharField(
        max_length=64,
        help_text="500 mt",
    )
    to_bus_station = models.CharField(
        max_length=64,
        help_text="200 mt",
    )
    to_city_center = models.CharField(
        max_length=64,
        help_text="5 km",
    )

    class Meta:
        db_table = "location_details"
        verbose_name = "Location Detail"
        verbose_name_plural = "Location Details"

    def __str__(self):
        return f"{self.google_map_url} - {self.zip_code}"
