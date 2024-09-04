from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.core.exceptions import ValidationError




class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.title




class Hashtag(models.Model):
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Хэштеги'
        verbose_name = 'Хэштег'

    def __str__(self):
        return self.title






class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    hashtags = models.ManyToManyField(Hashtag, null=True, related_name='hashtags')
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField(verbose_name="Описания", blank=True)
    image = models.ImageField()
    create_at = models.DateField(null=True)
    is_active = models.BooleanField(default=True)




    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'



class PublicationComment(models.Model):
    name = models.CharField(max_length=255, null=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)





class ClientContact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Клиент Контакты'
        verbose_name = 'Клиент Контакты'








