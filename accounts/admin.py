from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "name",
        "surname",
        "gender",
        "birthday",
        "country",
        "is_active",
        "is_staff",
        "date_joined",
    )
    list_filter = ("is_staff", "is_active", "country")
    search_fields = ("email", "name", "surname")
    ordering = ("date_joined",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "name",
                    "surname",
                    "gender",
                    "birthday",
                    "country",
                    "address",
                    "passport_no",
                    "passport_validation_start",
                    "passport_validation_end",
                    "user_currency",
                    "tel_no",
                    "image",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        # ("Important dates", {"fields": ("date_joined",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "surname",
                    "gender",
                    "birthday",
                    "country",
                    "address",
                    "passport_no",
                    "passport_validation_start",
                    "passport_validation_end",
                    "user_currency",
                    "tel_no",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )
    exclude = ("date_joined",)


admin.site.register(CustomUser, CustomUserAdmin)
