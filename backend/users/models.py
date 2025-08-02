from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Ensure staff access if admin OR superuser
        if self.is_admin or self.is_superuser:
            self.is_staff = True
        super().save(*args, **kwargs)
