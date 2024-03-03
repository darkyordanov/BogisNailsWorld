from django.db import models

from bogis_nails.core.models import Artist


class ArtistContacts(models.Model):
    # artist = models.ForeignKey(
    #     Artist,
    #     on_delete=models.DO_NOTHING,
    #     blank=False,
    #     null=False,
    # )
    
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
    
