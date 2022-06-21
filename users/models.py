from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name='email')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'