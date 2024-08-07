from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone



class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.title




class Hashtag(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Хэштеги'
        verbose_name = 'Хэштег'

    def __str__(self):
        return self.title






class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    hashtags = models.ManyToManyField(Hashtag, null=True)
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'


# class PublicationComment(models.Model):
#     publication = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True)
#
















