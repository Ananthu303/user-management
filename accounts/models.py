from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        OTHER = "Other", "Other"

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
