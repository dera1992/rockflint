# Generated by Django 2.2.5 on 2020-09-14 11:38

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191115_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='profile/None/no_image.png', height_field='height_field', null=True, upload_to=blog.models.upload_location, width_field='width_field'),
        ),
    ]
