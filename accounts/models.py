from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    class UserType(models.IntegerChoices):
        SUPERADMIN = 1, "SuperAdmin"
        USER = 3, "User"
    class GenderChoices(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        OTHER = "Other", "Other"

    username = models.CharField(max_length=100, unique=True)
    user_type = models.PositiveSmallIntegerField(choices=UserType.choices, default=UserType.USER)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
