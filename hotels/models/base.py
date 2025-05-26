import uuid
from django.db import models
from autoslug import AutoSlugField

from destinations.models import DestinationModel
from hotels.models.category import Category
from hotels.models.location import LocationDetails
from hotels.models.policy import Policy
from hotels.models.hotel_facility import GeneralFacility


class Hotel(models.Model):
    STARS = (
        ("1", "1 star"),
        ("2", "2 stars"),
        ("3", "3 stars"),
        ("4", "4 stars"),
        ("5", "5 stars"),
    )
    hotel_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
    )
    slug = AutoSlugField(
        unique=True,
        populate_from="title",
    )
    description = models.TextField(
        max_length=2000,
    )
    thumbnail = models.ImageField(
        upload_to="hotel_thumbnail",
    )
    stars = models.CharField(
        choices=STARS,
        blank=False,
        null=False,
    )
    # child_age_start = models.SmallIntegerField()
    child_age_end = models.SmallIntegerField(
        default=12,
        blank=False,
        null=False,
        help_text="Kaç yaşına kadar çocuk indirimi varsa",
    )
    destination = models.ForeignKey(
        to=DestinationModel,
        on_delete=models.DO_NOTHING,
        related_name="hotel_destination",
    )
    location = models.OneToOneField(
        to=LocationDetails,
        on_delete=models.CASCADE,
    )
    category = models.ManyToManyField(
        to=Category,
    )
    policies = models.ManyToManyField(
        to=Policy,
        help_text="+16 only, no single man",
    )
    reviews_frame = models.CharField(
        max_length=1000,
    )

    facilities = models.ManyToManyField(
        to=GeneralFacility,
        help_text="spa, asansör, pool",
    )
    # pansions
    # rooms_facilities

    def __str__(self):
        return str(self.title)
