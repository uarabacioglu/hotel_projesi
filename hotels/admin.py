from django.contrib import admin

from hotels.models.hotel_base import Hotel
from hotels.models.hotel_beach import Beach
from hotels.models.hotel_category import Category
from hotels.models.hotel_food_bevarage import FoodBevarage
from hotels.models.hotel_facility import GeneralFacility
from hotels.models.hotel_location import LocationDetails
from hotels.models.hotel_pool import Pool

from hotels.models.images import ImageModel, RoomImageModel
from hotels.models.policy import Policy

from hotels.models.room_base import Room
from hotels.models.room_block_dates import BlockDates
from hotels.models.room_facility import RoomFacilities
from hotels.models.room_penalty import Penalty
from hotels.models.room_pension import Pension
from hotels.models.room_periods import PeriodPricing


class ImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


class ImageInline(admin.StackedInline):
    model = ImageModel
    extra = 0


class RoomImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


class RoomImageInline(admin.StackedInline):
    model = RoomImageModel
    extra = 0


# # Block
class BlockPeriodAdmin(admin.ModelAdmin):
    list_display = ("blocked_date",)


class BlockInline(admin.StackedInline):
    model = BlockDates
    extra = 0


# # Period
class PeriodAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [BlockInline]


class PeriodInline(admin.StackedInline):
    model = PeriodPricing
    extra = 0


# # Room
class RoomAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [RoomImageInline, PeriodInline]


class RoomInline(admin.StackedInline):
    model = Room
    extra = 0


# # Hotel
class HotelAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
        RoomInline,
    ]
    search_fields = ("title",)
    list_display = ("title",)
    list_filter = ("destination",)
    list_per_page = 20

    def destination_title(self, hotel):
        return hotel.destination.title


admin.site.register(Hotel, HotelAdmin)
admin.site.register(ImageModel, ImageAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(BlockDates, BlockPeriodAdmin)
admin.site.register(PeriodPricing, PeriodAdmin)
admin.site.register(Beach)
admin.site.register(Category)
admin.site.register(FoodBevarage)
admin.site.register(GeneralFacility)
admin.site.register(LocationDetails)
admin.site.register(Penalty)
admin.site.register(Pension)
admin.site.register(Policy)
admin.site.register(Pool)
admin.site.register(RoomFacilities)
