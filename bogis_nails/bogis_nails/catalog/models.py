from django.db import models


class NailDesign(models.Model):
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
    
    # TODO: Make it like a ModelMixin 
    image = models.ImageField(
        upload_to='nail_images/'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    
    modified_at = models.DateTimeField(
        auto_now=True,
    )
    
    def __str__(self) -> str:
        return self.title



# class SavedNailDesign(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     nail_design = models.ForeignKey(NailDesign, on_delete=models.CASCADE)
#     saved_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('user', 'nail_design')

#     def __str__(self):
#         return f"{self.user.username} saved {self.nail_design.title}"

# COLOR_CHOISES = (
#         ('DARK', 'Dark'),
#         ('LIGHT', 'Light'),
#         ('RED', 'Red'),
#         ('PINK', 'Pink'),
#         ('BLUE', 'Blue'),
#         ('PURPLE', 'Purple'),
#         ('WHITE', 'White'),
#         ('BLACK', 'Black'),
#         ('GOLD', 'Gold'),
#         ('YELLOW', 'Yellow'),
#         ('ORANGE', 'Orange'),
#         ('GREEN', 'Green'),
#         ('BROWN', 'Brown'),
#         ('GRAY', 'Gray'),
#     )