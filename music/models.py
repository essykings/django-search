from statistics import mode
from django.db import models

# Create your models here.


class Music(models.Model):
    title = models.CharField(max_length= 255, null= False, blank=False)
    artist = models.CharField(max_length= 255, null= False, blank= False)

    def __str__(self):
        return self.title
