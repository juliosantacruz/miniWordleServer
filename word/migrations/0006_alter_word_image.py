# Generated by Django 5.0.7 on 2024-07-28 02:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0005_word_image_url_alter_word_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
