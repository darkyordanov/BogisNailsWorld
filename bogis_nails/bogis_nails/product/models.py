from django.db import models


class Product(models.Model):
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
    
    # TODO: Make it like a ModelMixin 
    image = models.ImageField(
        upload_to='product_images/'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    
    modified_at = models.DateTimeField(
        auto_now=True,
    )
    
    def __str__(self) -> str:
        return self.title 