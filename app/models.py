from django.db import models

class Jewelry(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    shape = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    image = models.ImageField(upload_to='jewelry_images')

    def __str__(self):
        return self.name