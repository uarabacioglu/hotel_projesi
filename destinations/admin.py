from django.contrib import admin
from destinations.models import DestinationModel


class DestinationAdmin(admin.ModelAdmin):
    model = DestinationModel
    search_fields = ["title"]
    list_display = ["title"]


admin.site.register(DestinationModel, DestinationAdmin)
