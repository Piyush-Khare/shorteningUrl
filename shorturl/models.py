from shorturl.utils import create_short_url
from django.db import models
from .utils import create_short_url
# Create your models here.

class ShortUrl(models.Model):
    long_url = models.URLField(max_length=300)
    short_url= models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'


    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_short_url(self)
        
        super().save(*args, **kwargs)
    