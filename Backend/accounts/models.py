from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        RESTAURANT_MANAGER = "RESTAURANT_MANAGER", "Restaurant Manager"

    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.CUSTOMER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email