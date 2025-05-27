import uuid
from django.db import models
from hotels.models.hotel_base import Hotel
from hotels.models.room_penalty import Penalty
from hotels.models.room_pension import Pension
from hotels.models.policy import Policy
from hotels.models.room_facility import RoomFacilities


class Room(models.Model):
    room_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    title = models.CharField(
        max_length=256,
        help_text="Sea view, Mountain view",
    )
    short_description = models.CharField(
        max_length=256,
        help_text="twin beds, queen bed",
    )
    hotel = models.ForeignKey(
        to=Hotel,
        on_delete=models.CASCADE,
        related_name="hotelrooms",
    )
    facilities = models.ManyToManyField(
        to=RoomFacilities,
        help_text="minibar",
    )
    pansion = models.ManyToManyField(
        to=Pension,
        help_text="all inclusive",
    )
    cancellation_penalty = models.ForeignKey(
        to=Penalty,
        on_delete=models.CASCADE,
        related_name="roompenalty",
    )
    policies = models.ManyToManyField(to=Policy)
    single_supplement = models.PositiveIntegerField(
        default=50,
        help_text="kişi başı gecelik pp fiyata + %single supplement uygulanır, pp 100 ise 150 gibi.",
    )
    triple_supplement = models.PositiveIntegerField(
        default=30,
        help_text="(kişi başı gecelik fiyat * 2) + (kişi başı gecelik fiyat / 100 * (100 - triple_supplement))",
    )
    family_supplement = models.PositiveIntegerField(
        default=3, help_text="kişi başı gecelik fiyat * family_supplement"
    )

    def __str__(self):
        return f"{self.hotel.title} - {self.title}"
