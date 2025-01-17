# Generated by Django 5.0.7 on 2024-08-05 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_publication_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='Category',
        ),
        migrations.AddField(
            model_name='publication',
            name='hashtags',
            field=models.ManyToManyField(null=True, to='blog.hashtag'),
        ),
        migrations.AddField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]
