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
    
    is_sale = models.BooleanField(
        default=False,
    )
    
    sale_price = models.DecimalField(
        default=0,
        max_digits=6,
        decimal_places=2,
    )
    
    def __str__(self) -> str:
        return self.title 
    
# class Order(models.Model):
#     product = models. ForeignKey(Product, on_delete=models.CASCADE)
#     customer = models. ForeignKey (Customer, on_delete=models.CASCADE)
#     quantity = models. IntegerField(default=1)
#     address = models. CharField(max_Length=100, default='',)
#     phone = models. CharField(max_Length=20, default='',)
#     date = models.DateField(default=datetime.datetime.today)
#     status = models.BooleanField(default=False)