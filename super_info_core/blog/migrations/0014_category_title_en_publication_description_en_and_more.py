# Generated by Django 5.0.7 on 2024-08-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_category_title_ky_category_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описания'),
        ),
        migrations.AddField(
            model_name='publication',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
    ]