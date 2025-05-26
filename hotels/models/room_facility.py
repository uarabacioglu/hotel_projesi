from django.db import models

class RoomFacilities(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text="TV, air-conditioning",
    )

    class Meta:
        db_table="room_facility"
        verbose_name="Room Facility"
        verbose_name_plural="Room Facilities"

    def __str__(self):
        return str(self.title)
