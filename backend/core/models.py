from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.is_staff = self.is_admin
        super().save(*args, **kwargs)
