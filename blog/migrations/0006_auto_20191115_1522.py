# Generated by Django 2.2.5 on 2019-11-15 14:22

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191115_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='profile/None/no-img.jpg', height_field='height_field', null=True, upload_to=blog.models.upload_location, width_field='width_field'),
        ),
    ]