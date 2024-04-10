from django.db import models
from django.contrib.auth import get_user_model

from bogis_nails.common.model_mixins import TimeStampedModel

UserModel = get_user_model()

class NailDesign(TimeStampedModel):    
    class Color(models.TextChoices):
        DARK = 'Dark', 'Dark'
        LIGHT = 'Light', 'Light'
        RED = 'Red', 'Red'
        PINK = 'Pink', 'Pink'
        BLUE = 'Blue', 'Blue'
        PURPLE = 'Purple', 'Purple'
        WHITE = 'White', 'White'
        BLACK = 'Black', 'Black'
        GOLD = 'Gold', 'Gold'
        NUDE = 'Nude', 'Nude'
        YELLOW = 'Yellow', 'Yellow'
        ORANGE = 'Orange', 'Orange'
        GREEN = 'Green', 'Green'
        BROWN = 'Brown', 'Brown'
        GRAY = 'Gray', 'Gray'

    class Size(models.TextChoices):
        SQUARE = 'Square', 'Square'
        ROUND = 'Round', 'Round'
        OVAL = 'Oval', 'Oval'
        ALMOND = 'Almond', 'Almond'
        STILETTO = 'Stiletto', 'Stiletto'
        COFFIN = 'Coffin', 'Coffin'

    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    colors = models.CharField(
        max_length=100,
        choices=Color.choices,
        blank=False,
        null=False,
    )
    
    size = models.CharField(
        max_length=20,
        choices=Size.choices,
        blank=False,
        null=False,
    )  
    
    image = models.ImageField(
        upload_to='nail_images/'
    )
    
    def __str__(self) -> str:
        return self.title


class Collection(models.Model):
    nails_designs = models.ManyToManyField(
        NailDesign,
    )
    
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='collection_user'
    )