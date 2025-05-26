from django.contrib import admin

from hotels.models.base import Hotel
from hotels.models.beach import Beach
from hotels.models.category import Category
from hotels.models.food_bevarage import FoodBevarage
from hotels.models.hotel_facility import GeneralFacility
from hotels.models.images import ImageModel
from hotels.models.location import LocationDetails
from hotels.models.penalty import Penalty
from hotels.models.pension_type import Pension
from hotels.models.policy import Policy
from hotels.models.pool import Pool
from hotels.models.room_facility import RoomFacilities
from hotels.models.room import Room


admin.site.register(Hotel)
admin.site.register(Beach)
admin.site.register(Category)
admin.site.register(FoodBevarage)
admin.site.register(GeneralFacility)
admin.site.register(ImageModel)
admin.site.register(LocationDetails)
admin.site.register(Penalty)
admin.site.register(Pension)
admin.site.register(Policy)
admin.site.register(Pool)
admin.site.register(RoomFacilities)
admin.site.register(Room)
