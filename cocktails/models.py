from django.db import models
from datetime import datetime


class Cocktail(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    instructions = models.TextField(blank=False, null=True)
    ingredient1 = models.CharField(max_length=120, null=True)
    ingredient2 = models.CharField(max_length=120, null=True)
    ingredient3 = models.CharField(max_length=120, null=True)
    ingredient4 = models.CharField(max_length=120, null=True)
    glass = models.CharField(max_length=120, null=True)
    measure1 = models.CharField(max_length=120,  null=True)
    measure2 = models.CharField(max_length=120,  null=True)
    measure3 = models.CharField(max_length=120,  null=True)
    measure4 = models.CharField(max_length=120,  null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',  height_field=None, width_field=None, max_length=None, null=True)
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
