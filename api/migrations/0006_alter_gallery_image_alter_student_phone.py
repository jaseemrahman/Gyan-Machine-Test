# Generated by Django 5.0.1 on 2024-01-25 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_imagemodel_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload JPG or PNG only', null=True, upload_to='gallery', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
