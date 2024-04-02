from django.db import models

from bogis_nails.common.model_mixins import TimeStampedModel
from bogis_nails.core.models import Artist


class ArtistContacts(TimeStampedModel):    
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    
    email = models.EmailField(
        blank=True,
        null=True,
    )
    
    address = models.TextField(
        blank=True,
        null=True,
    )
    
    def __str__(self) -> str:
        return 'Contact Information'
    
