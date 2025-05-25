from accounts.choices import COUNTRY_CHOICES, CURRENCY_CHOICES, GENDER_CHOICES
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email address must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    country = models.CharField(max_length=3, choices=COUNTRY_CHOICES)
    address = models.TextField(null=True, blank=True)
    passport_no = models.CharField(max_length=20, unique=True)
    passport_validation_start = models.DateField()
    passport_validation_end = models.DateField()
    user_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    tel_no = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Add related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(
        "auth.Group", related_name="customuser_groups", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="customuser_permissions", blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "surname", "birthday", "gender"]

    def __str__(self):
        return f"{self.name} - {self.surname} - ({self.email})"

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
        db_table = "accounts"
