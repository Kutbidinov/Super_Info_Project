from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Danislan(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    tall = models.FloatField()
    birth_date = models.DateField()
    image = models.ImageField(null=True)


