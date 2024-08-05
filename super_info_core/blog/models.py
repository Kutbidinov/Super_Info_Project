from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Publication(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'



class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'




class Hashtag(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Хэштеги'
        verbose_name = 'Хэштег'



