from django.db import models

# Create your models here.

class Images(models.Model):
    mediaTitle=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    mediaSource=models.CharField(max_length=100)
    mediaType=models.CharField(max_length=100)
    keywords=models.CharField(max_length=100)
    image=models.ImageField()


    def __str__(self):
        return self.mediaType
