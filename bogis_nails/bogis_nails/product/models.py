from django.db import models

from bogis_nails.common.model_mixins import TimeStampedModel


class Product(TimeStampedModel):
    title = models.CharField(
        max_length=36,
        blank=True,
        null=True,
    )
    
    description = models.TextField()
    
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    
    quantity = models.PositiveIntegerField(
        default=0,
    )
    
    image = models.ImageField(
        upload_to='product_images/'
    )
    
    def __str__(self) -> str:
        return self.title 