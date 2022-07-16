from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.CharField(max_length=64, null=False, blank=False, unique=True)
    password = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # Set email as username_field
    USERNAME_FIELD = 'email'

    class Meta:
        managed = True
        db_table = 'user'
