import uuid
from django.db import models
from autoslug import AutoSlugField
import PIL.Image


class DestinationModel(models.Model):
    destination_id = models.UUIDField(
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
        populate_from="title",
        unique=True,
        blank=False,
        null=False,
    )

    image = models.ImageField(
        upload_to="dest_images",
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"
        db_table = "destinations"

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        """Resmi yeniden boyutlandır ve kaydet."""
        super().save(*args, **kwargs)

        if self.image:
            image_path = self.image.path
            try:
                img = PIL.Image.open(image_path)

                if img.format not in ["JPEG", "JPG", "PNG"]:
                    raise ValueError("Unsupported image format.")

                width, height = img.size
                target_width = 800

                if width > target_width:
                    h_coefficient = width / target_width
                    target_height = height / h_coefficient
                    img = img.resize((int(target_width), int(target_height)))
                    img.save(image_path, quality=100)

                img.close()

            except Exception as e:
                print(f"Error processing image for ThumbnailModel: {e}")
