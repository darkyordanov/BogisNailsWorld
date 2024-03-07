from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import Group


class CustomUser(AbstractUser):
    birth_date = models.DateField(
        default=None,
        blank=True,
        null=True,
    )
    
    account_picture = models.ImageField(
        upload_to='account_pictures/',
        
    )
    
    def __str__(self):
        return self.username