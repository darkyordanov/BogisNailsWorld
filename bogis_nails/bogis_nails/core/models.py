from django.db import models


class Artist(models.Model):
    first_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    
    last_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    
    bio = models.TextField(
        blank=False,
        null=False,
    )
    
    certificates = models.ImageField(
        upload_to='artist_certificates_photos/',
    )
    
    
    photo = models.ImageField(
        upload_to='artist_photos/',
    )
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class HomePageContent(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.title
